from django.forms import ModelForm, TextInput
# ModelForm的運作原理，基本上就是跟某一個model裡面的table去做連動
# 所以只要ModelForm被操作的時候，它就會連帶地去更改資料庫中某table的內容
from datetime import date
from .models import Record, Category


#接下來要做的是繼承ModelForm生成一個物件
class RecordForm(ModelForm): #要生成的物件叫做 RecordForm，它要繼承ModelForm

	def __init__(self,user,*args,**kwargs):
		super().__init__(*args, **kwargs)
		by_user = Category.objects.filter(user=user) | Category.objects.filter(pk=39)
		self.fields['category'].queryset = by_user


	# 定義一個叫 Meta的subclass
	class Meta:
		# 定義這個subclass的兩個屬性
		model = Record   # 定義我們要用models的哪個物件，來跟我們的RecordForm做連動
						# 這裡是用Record這個table物件

		fields = ['date', 'description', 'category', 'cash', 'balance_type']  
		 # 定義我們要用到 Record這個物件中的哪幾個欄位

		widgets = {
					'date':TextInput(
							attrs={
								'id':'datepicker1',
								'value':date.today().strftime("%Y-%m-%d")  #預設值，先用today()叫出今
								# 天的日期，再轉換日期顯示的格式
							}
						),
				}
		# 允許我們在特定的欄位下做客製化的處理; 我們必需傳給widgets這個屬性一個dictionary, key值
		# 就代表欄位，value值則是要客製化的內容
		# Textinput() 代表我們對這個欄位選用的是text這種可以輸入文字的input
		# attrs 這個參數允許我們針對這個input裡面要定義啥樣的屬性做設定
		 
