import os
import csv
from django.http import HttpResponse, JsonResponse

#Check View
def index(request):
    return HttpResponse("Hi Subham! \n All OK")

# Get the parent directory of the current file (i.e., calDemoDeploy)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Set CSV path in ../temp/results.csv
CSV_PATH = os.path.join(BASE_DIR, 'temp', 'results.csv')


# Store a sum in results.csv
def store_result(request):
    sum_value = request.GET.get('sum')

    try:
        # Try converting to integer only
        sum_int = int(sum_value)

        os.makedirs(os.path.dirname(CSV_PATH), exist_ok=True)

        with open(CSV_PATH, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([sum_int])

        return JsonResponse({'status': 'saved', 'value': sum_int})

    except (TypeError, ValueError):
        return JsonResponse({'status': 'error', 'message': 'Only integer values allowed'}, status=400)


# Return all stored results
def get_results(request):
    results = []
    if os.path.exists(CSV_PATH):
        with open(CSV_PATH, 'r') as csvfile:
            reader = csv.reader(csvfile)
            results = [row[0] for row in reader if row]
    return JsonResponse({'results': results})

# For CORS error handling
def my_view(request):
    data = {"message": "Hello from Django!"}
    response = JsonResponse(data)
    response["Access-Control-Allow-Origin"] = "http://127.0.0.1:5500"
    return response



