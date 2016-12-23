from django import forms
from django.contrib.auth.models import User
from .models import Profile, Question, Answer, Tag
from django.contrib.auth import authenticate 

class LoginForm(forms.Form):
	username = forms.CharField(label='User', max_length=20, error_messages={'required': 'Required login'})
	password = forms.CharField(label='Password', widget=forms.PasswordInput, error_messages={'required': 'Required password'})

	def clean(self):
		cleaned_data = super(LoginForm, self).clean()
		if not self.errors:
			user = authenticate(username=cleaned_data['username'], password=cleaned_data['password'])
			if user is None:
				raise forms.ValidationError('Username or password is wrong')
			self.user = user
		return cleaned_data

	def get_user(self):
		return self.user or None

class AnswerForm(forms.ModelForm):
	class Meta:
		model = Answer
		fields = ('content',)
		widgets = {'content': forms.Textarea(attrs={'rows': 4, 'cols': 70}),}

class QuestionForm(forms.ModelForm):
	class Meta:
		model = Question
		fields = ('title', 'content', 'tags')
		widgets = {'content': forms.Textarea(attrs={'rows': 4, 'cols': 70}),}

class UserSignupForm(forms.ModelForm):
	password2 = forms.CharField(label="Repeat password", widget=forms.PasswordInput)

	def clean_password2(self):
		if self.cleaned_data.get('password2') != self.cleaned_data.get('password'):
			raise forms.ValidationError("Password is not match")
		return self.cleaned_data

	def save(self, commit=True):
		user = super(UserSignupForm, self).save(commit=False)
		user.set_password(self.cleaned_data.get("password"))
		if commit:
			user.save()
		return user

	class Meta:
		model = User
		fields = ['username', 'email', 'password']
		widgets = { 'password': forms.PasswordInput(), }

class ProfileSignupForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('nickname', 'avatar')

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'email']		
