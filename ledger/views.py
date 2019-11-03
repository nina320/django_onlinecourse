# 定義了各種運算，之後會再詳細解釋

from django.shortcuts import render, HttpResponse, redirect
from .models import Record, Category
from .forms import RecordForm   # 引入後，我們要用在 index.html那邊
from django.contrib.auth.decorators import login_required

# render 可以讓django正確地回傳 template當中的html檔案

# Create your views here.
@login_required  # 告訴Django這些函數要在login的狀態下才能使用
def hello(request):
	# return HttpResponse('hello')

	# a = 100
	# return render(request,'app/Hello.html', {'amount':a})  #它需要三個參數
	# 第一個是 request, 代表的是使用者在輸入網址時發送的請求; 請求會被包裝成一個物件，經由這個參數傳遞進來
	# 第二個是我們 html 放的位置 (路徑從 template底下開始計算)
	# 第三個是當我們這支 function計算出某些結果，並且我們要將這些結果回傳給template使用時，會放在這
	# 如在現在這個例子，我們在template中只要用 amount就可取到 a (即100) 這個值

	return render(request,'app/haha.html', {})

@login_required
def b_dashboard(request):
	user = request.user  # 若有登入就可以取到
	# 創建一個RecordForm物件
	record_form = RecordForm(user = user, initial = {'balance_type':'支出'})
	# intial 這個參數是用來給其中幾個欄位預設值

	# 我們現在要透過 model的 orm 語法，去跟資料庫要我們所需要的記錄後，再把資料傳給 template
	records = Record.objects.filter(user = user)  # 把 Record這個Table中屬於這個user的所有的記錄都取出來
	# 參考: https://docs.djangoproject.com/en/2.2/ref/templates/language/

	income_list = [record.cash for record in records if record.balance_type == "收入"]
	outcome_list = [record.cash for record in records if record.balance_type == "支出"]
	income = sum(income_list) if len(income_list)>0 else 0
	outcome = sum(outcome_list) if len(outcome_list)>0 else 0
	net = income - outcome
	# 把 records, income, outcome, net等變數傳給了index.html這個template使用
	# return render(request,'app/index.html',{'records': records, 'income':income,
	# 										 'outcome':outcome, 'net':net})       
	# 若覺得每次新增一個變數，這裡也都要跟著增加很麻煩的話，可用 locals() 這個函數來取得現在這個函數底下所有的變數
	return render(request,'app/index.html',locals())

@login_required
def settings(request):
	user = request.user
	categorys = Category.objects.filter(user = user)
	return render(request, 'app/settings.html',locals())

@login_required
def addCategory(request):
	user = request.user
	if request.method == "POST":  # 若傳送方法是post, 才做下面的事情 (post方法會有 csrf 驗證機制，比較安全)
		posted_data = request.POST    # 透過 request.POST存取到用post傳送給server的data
		# 這個東西是個像 dictionary的物件
		category = posted_data['_add_category'] # 從<imput name="add_category">來的
		if category != "":
			Category.objects.get_or_create(category=category, user = user)  # 使用 get_or_create 來避免有重複的資料輸進去
		# (category=category) 把category這個欄位指定為剛剛傳進來的這個變數
		return redirect('/settings')  # 把上面的事情做完後，自動地回到這個url

@login_required
def deleteCategory(request, category):
	user = request.user
	Category.objects.filter(category = category, user = user).delete()
	return redirect('/settings')

@login_required
def addRecord(request):
	if request.method == "POST":
		user = request.user
		form = RecordForm(user, request.POST) # ModelForm的一個特殊用法: 我們可以直接給一個ModelForm物件一個dictionary
		# 就相當於給這個Form一個值; 這邊我們就直接把POST進來的dictionary物件給這個Form, 並且把它存為名為form的物件
		# 這個時候相當於我們把 Form的值都填滿了
		if form.is_valid():  # 檢查一下這個Form接收的值是不是都符合規定(例如字數限制等…)
			record = form.save(commit = False)  #若通過驗證，就把這個ModelForm取到的值存進去model了，這樣就完成了資料庫的更新了
			record.user = user
			record.save()
	return redirect('/') # 最後不管有沒有驗證成功，都返回首頁

@login_required
def deleteRecord(request):
	if request.method == "POST":
		id = request.POST['delete_val']  # 取得那筆要刪除的記錄的id
		Record.objects.filter(id = id).delete()
	return redirect('/')



