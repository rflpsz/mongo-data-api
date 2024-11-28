from flask import request, jsonify
from pymongo.errors import PyMongoError
from bson import ObjectId
from dateutil import parser
from . import update_one_bp
from config.database import get_mongo_client


@update_one_bp.route("/data/v1/action/updateOne", methods=["POST"])
def update_one():
    data = request.json

    data_source_name = data.get("dataSource")
    database_name = data.get("database")
    collection_name = data.get("collection")
    filter_query = data.get("filter")
    update_data = data.get("update")

    upsert = data.get("upsert", False)

    missing_fields = []
    if not data_source_name:
        missing_fields.append("dataSource")
    if not database_name:
        missing_fields.append("database")
    if not collection_name:
        missing_fields.append("collection")
    if filter_query is None:
        missing_fields.append("filter")
    if update_data is None:
        missing_fields.append("update")

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
        update_data = convert_special_types(update_data)

        result = collection.update_one(filter_query, update_data, upsert=upsert)

        response = {
            "matchedCount": result.matched_count,
            "modifiedCount": result.modified_count,
        }

        if result.upserted_id is not None:
            response["upsertedId"] = str(result.upserted_id)

        return jsonify(response), 200

    except PyMongoError as e:
        return jsonify({"error": str(e)}), 500

    except Exception as e:
        return jsonify({"error": "An unexpected error occurred"}), 500
