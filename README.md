# Ubuntu_Requests

## RequestsAssignments.py

This script allows users to download images from a given URL using the `requests` library in Python. It ensures proper handling of HTTP requests, file saving, and error management.

### Features
- Prompt user for an image URL.
- Automatically create a directory (`Fetched_Images`) to store downloaded images.
- Extract and handle filenames from URLs, with fallback for missing or invalid filenames.
- Download and save images efficiently using streaming.
- Gracefully handle HTTP and network errors.

### Requirements
- Python 3.6 or higher
- `requests` library

### Installation
1. Clone this repository:
    ```bash
    git clone https://github.com/your-username/Ubuntu_Requests.git
    ```
2. Navigate to the project directory:
    ```bash
    cd Ubuntu_Requests
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Usage
Run the script using Python:
```bash
python RequestsAssignments.py
```

### License
This project is licensed under the MIT License. See the LICENSE file for details.