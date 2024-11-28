from flask import request, jsonify
from pymongo.errors import PyMongoError
from bson import ObjectId, json_util
from dateutil import parser
from . import find_bp
from config.database import get_mongo_client


@find_bp.route("/data/v1/action/find", methods=["POST"])
def find_many():
    data = request.json

    data_source_name = data.get("dataSource")
    database_name = data.get("database")
    collection_name = data.get("collection")
    filter_query = data.get("filter", {})
    projection = data.get("projection", {})
    sort = data.get("sort")
    limit = data.get("limit")
    skip = data.get("skip")

    missing_fields = []
    if not data_source_name:
        missing_fields.append("dataSource")
    if not database_name:
        missing_fields.append("database")
    if not collection_name:
        missing_fields.append("collection")

    if missing_fields:
        return (
            jsonify({"error": f"Missing required fields: {', '.join(missing_fields)}"}),
            400,
        )

    try:
        client = get_mongo_client()
        db = client[database_name]
        collection = db[collection_name]

        def convert_special_types(obj):
            if isinstance(obj, dict):
                return {k: convert_special_types(v) for k, v in obj.items()}
            elif isinstance(obj, list):
                return [convert_special_types(i) for i in obj]
            elif isinstance(obj, str):
                if ObjectId.is_valid(obj):
                    return ObjectId(obj)
                try:
                    return parser.isoparse(obj)
                except ValueError:
                    return obj
            else:
                return obj

        filter_query = convert_special_types(filter_query)
        projection = convert_special_types(projection)
        if sort is not None:
            sort = convert_special_types(sort)

        cursor = collection.find(filter_query, projection)

        if sort:
            sort_list = []
            for key, value in sort.items():
                if value in [1, -1]:
                    sort_list.append((key, value))
                else:
                    return (
                        jsonify(
                            {
                                "error": f"Invalid sort value for field '{key}': {value}. Must be 1 or -1"
                            }
                        ),
                        400,
                    )
            cursor = cursor.sort(sort_list)

        if skip is not None:
            try:
                skip = int(skip)
                cursor = cursor.skip(skip)
            except ValueError:
                return (
                    jsonify({"error": "Invalid value for 'skip'. Must be an integer."}),
                    400,
                )

        if limit is not None:
            try:
                limit = int(limit)
                cursor = cursor.limit(limit)
            except ValueError:
                return (
                    jsonify(
                        {"error": "Invalid value for 'limit'. Must be an integer."}
                    ),
                    400,
                )

        results = list(cursor)

        json_results = json_util.dumps(results)

        return json_results, 200, {"Content-Type": "application/json"}

    except PyMongoError as e:
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred"}), 500
