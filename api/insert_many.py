from flask import request, jsonify
from pymongo.errors import PyMongoError
from bson import ObjectId
from dateutil import parser
from . import insert_many_bp
from config.database import get_mongo_client


@insert_many_bp.route("/data/v1/action/insertMany", methods=["POST"])
def insert_many():
    data = request.json

    data_source = data.get("dataSource")
    database_name = data.get("database")
    collection_name = data.get("collection")
    documents = data.get("documents")

    missing_fields = []
    if not data_source:
        missing_fields.append("dataSource")
    if not database_name:
        missing_fields.append("database")
    if not collection_name:
        missing_fields.append("collection")
    if documents is None:
        missing_fields.append("documents")

    if missing_fields:
        return (
            jsonify({"error": f"Missing required fields: {', '.join(missing_fields)}"}),
            400,
        )

    try:
        client = get_mongo_client()
        db = client[database_name]
        collection = db[collection_name]

        if not isinstance(documents, list):
            return (
                jsonify(
                    {"error": "The 'documents' field must be an array of documents"}
                ),
                400,
            )

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

        documents = [convert_special_types(doc) for doc in documents]

        result = collection.insert_many(documents)

        response = {
            "insertedIds": [str(inserted_id) for inserted_id in result.inserted_ids]
        }
        return jsonify(response), 200

    except PyMongoError as e:
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred"}), 500
