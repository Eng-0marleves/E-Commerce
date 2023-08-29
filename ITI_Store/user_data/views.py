from django.shortcuts import render
from .models import User
from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .srializers import UserSerializer
from django.contrib.auth import authenticate
from django.core.mail import send_mail
# from rest_framework_simplejwt.tokens import RefreshToken


def user(request, imgId):
	try:
		user = User.objects.get(id=imgId)
		return render(request, 'imgs/img.html', {'user': user})
	except User.DoesNotExist:
		raise Http404('User not found')


def signupPage(request):
	return render(request, 'signup.html')



# APIs

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


@api_view(['POST'])
def user_login(request):
	email = request.data.get('email')
	password = request.data.get('password')

	if email and password:
		user = authenticate(request, username=email, password=password)
		if user:
			refresh = RefreshToken.for_user(user)
			access_token = str(refresh.access_token)
			return Response({'token': access_token}, status=status.HTTP_200_OK)
		else:
			return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
	return Response({'error': 'Email and password are required'}, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['POST'])
# def user_signup(request):
# 	serializer = UserSerializer(data=request.data)
# 	if serializer.is_valid():
# 		user = serializer.save()

# 		subject = 'Welcome to Our App'
# 		message = 'Thank you for signing up!'
# 		from_email = 'noreply@example.com'
# 		recipient_list = [user.email]
# 		send_mail(subject, message, from_email, recipient_list)

# 		return Response({'success': 'User registered successfully'}, status=status.HTTP_201_CREATED)
# 	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

