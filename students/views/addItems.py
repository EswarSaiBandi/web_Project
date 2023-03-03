from django.contrib.auth.decorators import user_passes_test
from students.forms import *
from django.shortcuts import render

def customer_check(user):
    return user.is_authenticated  and user.is_customer 

# @user_passes_test(customer_check)
# def addItems(request):
#     user=request.user
#     model = item 
#     form_class = addItemsForm
#     template_name = 'students/addItems.html'
#     success_url = reverse_lazy('students:addItems')
#     success_message = 'Item successfully Added!'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['form_title'] = 'Add Items'
#         return context
#     def get_form_kwargs(self):
#         kwargs = super(addItems, self).get_form_kwargs()
#         kwargs['request'] = self.request
#         return kwargs
#     def form_valid(self, form):
#         # form.instance.student = self.request.user.student
#         return super().form_valid(form)


@user_passes_test(customer_check)
def addItems(request):
    if request.method == 'POST':
        form = addItemsForm(request.POST)
        if(form.is_valid()):
            item_id = form.cleaned_data['item_id']
            price = form.cleaned_data['price']
            quantity_available = form.cleaned_data['quantity_available']
            # regulation = int(form.cleaned_data['regulation'])
            if(( (form.cleaned_data['price']>=0) and (form.cleaned_data['quantity_available']>0))):
                r = item(item_id=item_id, quantity_available=quantity_available, price=price)
                r.save()
                msg = 'Regulation Added Successfully.'
                return render(request, 'students/addItems.html', {'form':form, 'msg':msg})
    else:
        form = addItemsForm()
    return render(request, 'students/addItems.html', {'form':form})