# 🔄 MongoDB Data API Alternative

With the **MongoDB Data API** being discontinued in **September 2025**, this **Flask REST API** provides a comprehensive, drop-in replacement solution for developers and projects impacted by the service shutdown.

## 🌟 Overview

This project offers a fully-featured RESTful interface that replicates MongoDB's core CRUD and aggregation operations. Designed to be seamlessly integratable, extensible, and stable, it serves as a robust alternative to the official MongoDB Data API.

---

## 🚀 Key Features

### Comprehensive Data Operations
- **CRUD Functionality**:
  - Document Insertion (`insertOne`, `insertMany`)
  - Document Retrieval (`find`, `findOne`)
  - Document Update (`updateOne`, `updateMany`)
  - Document Deletion (`deleteOne`, `deleteMany`)

### Advanced Capabilities
- **Aggregation Support**:
  - Full pipeline aggregation operations
- **MongoDB Compatibility**:
  - Comprehensive support for:
    - Filters
    - Projections
    - Sorting
    - Pagination
    - Skipping
- **Automatic Type Conversion**:
  - Seamless handling of complex types (ObjectId, ISO8601 dates)

### Enterprise-Grade Features
- **Security**:
  - CORS support for secure cross-application integration
- **Extensibility**:
  - Easily configurable and adaptable to diverse requirements

---

## 🛠️ Technology Stack

- **[Flask](https://flask.palletsprojects.com/)**: Lightweight and efficient web framework
- **[MongoDB](https://www.mongodb.com/)**: NoSQL database backend
- **[Flasgger](https://github.com/flasgger/flasgger)**: Automatic Swagger API documentation
- **[Flask-CORS](https://flask-cors.readthedocs.io/)**: Cross-Origin Resource Sharing configuration

---

## 📡 API Endpoints

### Base URL
```
http://<host>:<port>/api/data/v1/action/<operation>
```

### Supported Operations

| HTTP Method | Endpoint       | Description                        |
|------------|----------------|-------------------------------------|
| POST       | `/insertOne`   | Insert a single document           |
| POST       | `/insertMany`  | Insert multiple documents          |
| POST       | `/findOne`     | Retrieve a single document         |
| POST       | `/find`        | Retrieve multiple documents        |
| POST       | `/updateOne`   | Update a single document           |
| POST       | `/updateMany`  | Update multiple documents          |
| POST       | `/deleteOne`   | Delete a single document           |
| POST       | `/deleteMany`  | Delete multiple documents          |
| POST       | `/aggregate`   | Execute aggregation pipeline       |

---

## 🔧 Setup and Installation

### Prerequisites
- Python 3.8+
- MongoDB 4.0+

### Local Development

1. **Clone the Repository**
   ```bash
   git clone https://github.com/rflpsz/mongo-data-api
   cd mongo-data-api
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   # Activate the virtual environment
   # Linux/Mac: 
   source venv/bin/activate
   # Windows: 
   venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**
   Create a `.env` file with the following configuration:
   ```bash
   DB_USERNAME=<your_username>
   DB_PASSWORD=<your_password>
   DB_HOST=<your_hostname>
   DB_CLUSTER_NAME=<your_cluster>
   ```

5. **Run the Application**
   ```bash
   python app.py
   ```

### Docker Deployment

For containerized deployment, use the included Dockerfile and docker-compose.yml:

```bash
docker-compose up --build
```

### Access the API
- Local: `http://localhost:5000/api/data/v1/action/`
- Swagger Documentation: `http://localhost:5000/apidocs/`

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

Free to use.

## 📧 Contact

### Project Maintainers

**Rafael Souza**
- 💼 LinkedIn: [Rafael Souza](https://www.linkedin.com/in/rafaelpereirasouza/)
- 🐱 GitHub: [rflpsz](https://github.com/rflpsz)

**Allyson Paulino**
- 💼 LinkedIn: [Allyson Paulino](https://www.linkedin.com/in/allyson-paulino-0694a973/)
- 🐱 GitHub: [allysonpaulino](https://github.com/allysonp23)

### 🚀 Get Involved
- Report issues: [Project Issues](https://github.com/rflpsz/mongo-data-api/issues)
- Request features: [Feature Requests](https://github.com/rflpsz/mongo-data-api/issues)

### 📬 Support
For questions, support, or collaboration, please open an issue on our GitHub repository or contact the maintainers directly.
