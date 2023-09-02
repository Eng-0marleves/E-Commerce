# from django.shortcuts import redirect, render
# from .models import User
# from django.http import Http404
# from rest_framework.decorators import api_view
# from rest_framework import status
# from rest_framework.response import Response
# from .srializers import UserSerializer
# from django.core.mail import send_mail







# def homePage(request):
# 	return render(request, 'home.html')


# # APIs

# @api_view(['GET'])
# def git_user_info(request, user_id):
# 	res_obj = {}
# 	serializedUser = {}
# 	http_status = status.HTTP_200_OK
# 	try:
# 		user = User.objects.get(id=user_id)

# 		if user:
# 			serializedUser = UserSerializer(user)
# 			res_obj['success'] = True
# 			res_obj['data'] = serializedUser.data
# 			res_obj['error'] = None
# 	except Exception as e:
# 		print(f"exceotion in user_info => {e}")
# 		res_obj['success'] = False
# 		res_obj['data'] = None
# 		res_obj['error'] = f'{e}'
# 		http_status = status.HTTP_500_INTERNAL_SERVER_ERROR
# 	return Response(data=res_obj, status=http_status)



# # @api_view(['POST'])
# # def user_login(request):
# # 	email = request.data.get('email')
# # 	password = request.data.get('password')

# # 	if email and password:
# # 		user = authenticate(request, username=email, password=password)
# # 		if user:
# # 			refresh = RefreshToken.for_user(user)
# # 			access_token = str(refresh.access_token)
# # 			return Response({'token': access_token}, status=status.HTTP_200_OK)
# # 		else:
# # 			return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
# # 	return Response({'error': 'Email and password are required'}, status=status.HTTP_400_BAD_REQUEST)










from django.http import Http404
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .srializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from django.shortcuts import redirect, render
from django.core.files.storage import default_storage
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import check_password
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.exceptions import AuthenticationFailed
from django.core.mail import send_mail


class UserInfoView(APIView):
	permission_classes = [IsAuthenticated]

	def get(self, request):
		user = request.user
		serializer = UserSerializer(user)
		return Response(serializer.data)



class UserInfoViewSet(ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = [IsAuthenticated]

	def get_object(self):
		return self.request.user


class SignupView(TemplateView):
	template_name = 'signup.html'


class SignupAPIView(APIView):
	def post(self, request):
		serializer = UserSerializer(data=request.data)

		if serializer.is_valid():
			email = serializer.validated_data['email']
			password = serializer.validated_data['password']
			confirm_password = request.data.get('confirm_password')

			if password != confirm_password:
				return redirect('view-signup')

			if User.objects.filter(email=email).exists():
				return redirect('view-signup')

			serializer.save()
			return redirect('home-page')

		return redirect('view-signup')


class LoginView(TemplateView):
	template_name = 'login.html'

class LoginAPIView(APIView):

	def post(self, request):

		email = request.data.get('email')
		password = request.data.get('password')

		user = authenticate(email=email, password=password)

		if user is not None:
			login(request, user)
			return redirect('home-page')

		else:
			raise AuthenticationFailed('Invalid credentials')

def homePage(request):
	return render(request, 'home.html')



def profilePage(request):
	return render(request, 'profile.html')



@api_view(['GET'])
def git_user_info(request, user_id):
	res_obj = {}
	serializedUser = {}
	http_status = status.HTTP_200_OK
	try:
		user = User.objects.get(id=user_id)

		if user:
			serializedUser = UserSerializer(user)
			res_obj['success'] = True
			res_obj['data'] = serializedUser.data
			res_obj['error'] = None
	except Exception as e:
		print(f"exceotion in user_info => {e}")
		res_obj['success'] = False
		res_obj['data'] = None
		res_obj['error'] = f'{e}'
		http_status = status.HTTP_500_INTERNAL_SERVER_ERROR
	return Response(data=res_obj, status=http_status)


# views.py


@api_view(['GET'])
def get_user_by_id(request, user_id):

	if request.method == 'GET':

		try:
			user = User.objects.get(id=user_id)

		except User.DoesNotExist:
			return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

		serializer = UserSerializer(user)
		return Response(serializer.data)

	else:
		return Response({'error': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)






@api_view(['POST'])
def get_user_by_email(request):

	if request.method == 'POST':

		email = request.data.get('email')
		password = request.data.get('password')

		try:
			user = User.objects.get(email=email)

		except User.DoesNotExist:
			return Response({'error':'Invalid email'}, status=status.HTTP_404_NOT_FOUND)

		if not user.check_password(password):
			return Response({'error':'Invalid password'}, status=status.HTTP_401_UNAUTHORIZED)

		serializer = UserSerializer(user)
		return Response(serializer.data)

	else:
		return Response({'error': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


def user_image(request, imgId):
	try:
		user = User.objects.get(id=imgId)
		return render(request, 'imgs/img.html', {'user': user})
	except User.DoesNotExist:
		raise Http404('User not found')



def signupPage(request):
	if request.method == 'POST':
		first_name = request.post.get('first_name')
		last_name = request.post.get('last_name')
		email = request.post.get('email')
		pass1 = request.post.get('pass1')
		pass2 = request.post.get('pass2')
		# my_user = User.objects.create(username=first_name, email=email)
		print(first_name, last_name, email, pass1, pass2)

	return render(request, 'signup.html')



@api_view(['POST'])
def user_signup(request):
	if request.method == 'POST':
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		email = request.POST.get('email')
		password = request.POST.get('password')

		User.objects.save()

		subject = 'Welcome to Our App'
		message = 'Thank you for signing up!'
		from_email = 'noreply@example.com'
		recipient_list = [email]
		send_mail(subject, message, from_email, recipient_list)

		return redirect('home-page')

	return render(request, 'signup.html')

@api_view(['PUT'])
def update_user_info(request, user_id):
	try:
		user = User.objects.get(id=user_id)
	except User.DoesNotExist:
		return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

	if request.method == 'PUT':
		serializer = UserSerializer(user, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({'success': 'User information updated'}, status=status.HTTP_200_OK)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def loginPage(request):
	return render(request, 'login.html')