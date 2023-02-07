from django.shortcuts import render, redirect
from .forms import CustomerForm
from .models import Customer
import pandas as pd
import matplotlib.pyplot as plt
import base64
import io


# Create your views here.
def create_customer(request):
  if request.method == 'POST':
    form = CustomerForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('customer_list')
  else:
    form = CustomerForm()
    return render(request, 'customer_form.html', {'form': form})


def customer_list(request):
  customers = Customer.objects.all(Customer)
  months = []
  incomes = []
  expenses = []

  # read data from the uploaded excel file
  # using a for loop

  for customer in customers:
      wb = openpyxl.load_workbook(customer.excel_file.path)
      sheet = wb['Sheet1']
      for row in range(2, sheet.max_row + 1):
        month = sheet.cell(row=row, column=1).value
        income = sheet.cell(row=row, column=2).value
        expense = sheet.cell(row=row, column=3).value
        months.append(month)
        incomes.append(income)
        expenses.append(expense)

# plot the line graph using matplotlib

  fig, ax = plt.subplots()
  ax.plot(months, incomes, label='Income')
  ax.plot(months, expenses, label='Expenses')
  ax.set(xlabel='Month', ylabel='Amount', title='Income vs Expenses')
  ax.legend()

    # convert the plot to a PNG image and save it as a base64 encoded string

  buf = io.BytesIO()
  plt.savefig(buf, format='png')
  buf.seek(0)
  image_base64 = base64.b64encode(buf.read()).decode('utf-8').replace('\n', '')
  plt.close(fig)

  return render(request, 'customer/customer_list.html', {'customers': customers, 'graph': image_base64})

    