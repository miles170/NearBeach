from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import  loader
from NearBeach.forms import *
from .models import *
from NearBeach.models import *



@login_required(login_url='login')
def line_items(request, quote_id):
    # Load the template
    t = loader.get_template('NearBeach/quote_information_modules/line_items.html')

    # context
    c = {
        'quote_id': quote_id,
    }

    return HttpResponse(t.render(c, request))



@login_required(login_url='login')
def new_line_item(request,quote_id):
    if request.POST:
        form = new_line_item_form(request.POST, request.FILES)
        if form.is_valid():
            #All data
            extracted_product_and_services = form.cleaned_data['products_and_services']
            quantity = form.cleaned_data['quantity']
            product_description = form.cleaned_data['product_description']
            product_cost = form.cleaned_data['product_cost']
            discount_choice = form.cleaned_data['discount_choice']
            discount_percent = form.cleaned_data['discount_percent']
            discount_amount = form.cleaned_data['discount_amount']
            product_price = form.cleaned_data['product_price']
            tax = form.cleaned_data['tax']
            tax_amount = form.cleaned_data['tax_amount']
            total = form.cleaned_data['total']
            product_note = form.cleaned_data['product_note']

            #Instances needed
            quote_instance = quotes.objects.get(quote_id=quote_id)
            product_instance = products_and_services.objects.get(product_name = extracted_product_and_services)

            #Check to make sure they are not blank - default = 0
            if ((discount_percent == '') or (not discount_percent)): discount_percent = 0
            if ((discount_amount == '') or (not discount_amount)) : discount_amount = 0


            print("products_and_services: " + str(products_and_services))
            print("quantity: " + str(quantity))
            print("product_description: " + str(product_description))
            print("product_cost: " + str(product_cost))
            print("discount_choice: " + str(discount_choice))
            print("discount_percent: " + str(discount_percent))
            print("discount_amount: " + str(discount_amount))
            print("product_price: " + str(product_price))
            print("tax: " + str(tax))
            print("tax_amount: " + str(tax_amount))
            print("total: " + str(total))
            print("product_note: " + str(product_note))
            print("quote_id: " + str(quote_instance))


            #Save line item
            submit_line_item = quotes_products_and_services(
                products_and_services = product_instance,
                quantity = quantity,
                product_description = product_description,
                product_cost = product_cost,
                discount_choice = discount_choice,
                discount_percent = discount_percent,
                discount_amount = discount_amount,
                product_price = product_price,
                tax = tax,
                tax_amount = tax_amount,
                total = total,
                product_note = product_note,
                change_user=request.user,
                quote_id=quote_instance.quote_id,
            )
            submit_line_item.save()



        else:
            print(form.errors)

    # Load the template
    t = loader.get_template('NearBeach/quote_information_modules/new_line_item.html')

    # context
    c = {
        'quote_id': quote_id,
        'new_line_item_form': new_line_item_form(),
    }

    return HttpResponse(t.render(c, request))


