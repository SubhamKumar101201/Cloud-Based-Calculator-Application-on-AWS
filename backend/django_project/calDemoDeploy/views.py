import os
import csv
from django.http import HttpResponse, JsonResponse

#Check View
def index(request):
    return HttpResponse("Hi Subham! \n All OK")



# Store a sum in results.csv
def store_result(request):
    sum_value = request.GET.get('sum')

    try:
        # Try converting to integer only
        sum_int = int(sum_value)

        file_path = os.path.join(os.path.dirname(__file__), 'results.csv')
        with open(file_path, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([sum_int])

        return JsonResponse({'status': 'saved', 'value': sum_int})

    except (TypeError, ValueError):
        return JsonResponse({'status': 'error', 'message': 'Only integer values allowed'}, status=400)


# Return all stored results
def get_results(request):
    file_path = os.path.join(os.path.dirname(__file__), 'results.csv')
    results = []
    if os.path.exists(file_path):
        with open(file_path, 'r') as csvfile:
            reader = csv.reader(csvfile)
            results = [row[0] for row in reader if row]
    return JsonResponse({'results': results})

# For CORS error handling
def my_view(request):
    data = {"message": "Hello from Django!"}
    response = JsonResponse(data)
    response["Access-Control-Allow-Origin"] = "http://127.0.0.1:5500"
    return response