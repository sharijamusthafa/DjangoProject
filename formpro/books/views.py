from django.shortcuts import render,redirect
from books.models import Book
from books.forms import BookCreateForm
from books.models import Book
# Create your views here.

def bookCreate(request):
    template_name="bookcreate.html"
    form=BookCreateForm()
    context={}
    books=Book.objects.all()
    context["books"]=books
    context["form"]=form
    if request.method=="POST":
        form=BookCreateForm(request.POST)
        if form.is_valid():
            book_name=form.cleaned_data.get("book_name")
            author=form.cleaned_data.get("author")
            price=form.cleaned_data.get("price")
            pages=form.cleaned_data.get("pages")
            obj=Book(book_name=book_name,author=author,price=price,pages=pages)
            obj.save()
            qs=Book.objects.all()
            context["books"]=qs
            return redirect("li")

    return render(request,template_name,context)

def listBook(request):
    template_name="list.html"
    qs=Book.objects.all()
    context={}
    context["items"]=qs
    return render(request,template_name,context)

def viewBook(request,idd):
    template_name="viewbk.html"
    qs=Book.objects.get(id=idd)
    dict={}
    dict["itemm"]=qs
    return render(request,template_name,dict)

def deleteBook(request,idd):

    qs=Book.objects.get(id=idd).delete()
    return redirect("li")
def updateBook(request,idd):
    pe=Book.objects.get(id=idd)
    form=BookCreateForm(instance=pe)
    context={}
    context["form"]=form

    if request.method=="POST":
        form=BookCreateForm(instance=pe,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("li")
    return render(request,"updbk.html",context)
