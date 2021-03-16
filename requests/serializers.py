from rest_framework import serializers
from .models import SolicitacaoTransito, SolicitacaoEducacao, SolicitacaoIluminacao, SolicitacaoMeioAmbiente, Endereco
from users.models import ProfileUser

class TransitoSerializer(serializers.ModelSerializer):
	class Meta:
		model = SolicitacaoTransito
		fields = ['pk', 'nome', 'email', 'tipo', 'endereco', 'data_criacao', 'comentario', 'imagem', ]

class EducacaoSerializer(serializers.ModelSerializer):
	class Meta:
		model = SolicitacaoEducacao		
		fields = ['pk', 'nome', 'email', 'cadastro_pf', 'rg', 'escola', 'data_criacao', 'comentario',]

class IluminacaoSerializer(serializers.ModelSerializer):
	class Meta:
		model = SolicitacaoIluminacao
		fields = ['pk', 'nome', 'email', 'conta_luz', 'rg', 'data_criacao', 'comentario',]

class MeioAmbienteSerializer(serializers.ModelSerializer):
	class Meta:
		model = SolicitacaoMeioAmbiente
		fields = ['pk', 'nome', 'email', 'endereco',]
		
class EnderecoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Endereco
		fields = ['pk', 'bairro', 'rua', 'numero', 'complemento',]
        
class RegistrationSerializer(serializers.ModelSerializer):    
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    
    class Meta:
        model = ProfileUser
        fields = ['email', 'nome', 'password', 'password2']
        extra_kwargs = {
                'password': {'write_only': True}
        }
   
    def save(self):
        user = ProfileUser(
            email = self.validated_data['email'],
            nome = self.validated_data['nome'],
        )

        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        
        if password != password2:
            raise serializers.ValidationError({'password': 'As senhas precisam ser iguais.'})
        user.set_password(password)
        user.save()
        return user

        