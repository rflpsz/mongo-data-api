from flask import request, jsonify
from pymongo.errors import PyMongoError
from bson import ObjectId, json_util
import dateutil.parser
from . import find_one_bp
from config.database import get_mongo_client


@find_one_bp.route("/data/v1/action/findOne", methods=["POST"])
def find_one():
    data = request.json

    data_source_name = data.get("dataSource")
    database_name = data.get("database")
    collection_name = data.get("collection")
    filter_query = data.get("filter", {})
    projection = data.get("projection", {})

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
                    return dateutil.parser.isoparse(obj)
                except ValueError:
                    return obj
            else:
                return obj

        filter_query = convert_special_types(filter_query)
        projection = convert_special_types(projection)

        result = collection.find_one(filter_query, projection)

        if result:
            json_result = json_util.dumps(result)
            return json_result, 200, {"Content-Type": "application/json"}
        else:
            return jsonify({"message": "Document not found"}), 200

    except PyMongoError as e:
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred"}), 500
