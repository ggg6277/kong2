from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import RstForm, ImageForm, PrdctFrom, CommentForm, BlogwriteForm
from .models import Test, Image, Product, Comment, Post


def index(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = RstForm(request.POST, request.FILES)
        if form.is_valid():
            test = Test(
                subject=form.cleaned_data["subject"],
                summary=form.cleaned_data["summary"],
                upload_date=form.cleaned_data["upload_date"],
                image=form.cleaned_data["image"],
                acount=form.cleaned_data["acount"],
            )
            test.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'testgallery.html', {'form': form, 'img_obj': img_obj})
    else:
        form = RstForm()
    return render(request, 'testgallery.html', {'form': form})

def addproduct(request):
    if request.method=='POST':
        form = PrdctFrom(request.POST)
        if form.is_valid():
            product = Product(
                code=form.cleaned_data["code"],
                product=form.cleaned_data["product"],
                price=form.cleaned_data["price"],
                exp_date=form.cleaned_data["exp_date"],
            )
            product.save()
            # Get the current instance object to display in the template
            return render(request, 'product.html', {'form': form})
    else:
        form = PrdctFrom()
    return render(request, 'product.html', {'form': form})

def product_detail(request):
    products=Product.objects.all()
    context={
        "products": products,
    }
    return render(request, "productdetail.html", context)

def structure(request):
    tests = Test.objects.all()
    context={
        "tests":tests,
    }
    return render(request, "structure.html", context)

def showindex(request):
    tests = Test.objects.all().order_by('-upload_date')
    context={
        "tests":tests,
    }
    return render(request, "showindex.html", context)

def showdetail(request, pk):
    tests = Test.objects.get(pk=pk)
    context={
        'tests':tests,
    }
    return render(request, 'showdetail.html', context)

def image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image1= Image(
                title=form.cleaned_data["title"],
                image=form.cleaned_data["image"],
            )
            image1.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'image.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'image.html', {'form': form})

def cat(request):

    return render(request, 'act.html')

def mainsite(request):
    return render(request, 'mainsite.html')
def banana(request):
    return render(request, 'banana.html')

def apple(request):
    return render(request, 'apple.html')

def blog(request):
    return render(request, 'blog.html')

def base(request):
    return render(request, 'base.html')

def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    paginator = Paginator(posts, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "posts":posts,
        "page_obj" : page_obj,
    }
    return render(request, "blog_index.html", context)

def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post = post)

    if request.method =="POST":
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = Comment(
                author = form.cleaned_data["author"],
                body = form.cleaned_data["body"],
                post = post,
            )
            comment.save()
        context = {"post": post,
                   "comments": comments,
                   "form": form}
        return render(request, "blog_detail.html", context)
    else:
        form=CommentForm()
        context={
            "post":post,
            "comments":comments,
            "form":form
        }
    return render(request, "blog_detail.html", context)

def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context={
        "category": category,
        "posts": posts
    }
    return render(request, "blog_category.html", context)

def blog_write(request):
    if request.method =="POST":
        form = BlogwriteForm(request.POST)
        new = form.save(commit=False)

        if form.is_valid():
            post = Post(
                title=form.cleaned_data["title"],
                body=form.cleaned_data["body"]
            )
            new.save()
            form.save_m2m()
            return redirect('blog_index')
    else:
        form= BlogwriteForm()
    return render(request, "blog_write.html", {'form': form})

def album(request):
    tests = Test.objects.all().order_by('-upload_date')
    context = {
        "tests": tests,
    }
    return render(request, 'Album_base.html', context)

def album_detail(request, pk):
    tests = Test.objects.get(pk=pk)
    context = {
       "tests": tests,
    }
    return render(request, 'album_detail.html', context)

def signup(request):
    if request.method=="POST":
        form= UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
        return render (request, 'signup.html', ['form': form])

