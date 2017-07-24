#Copyright (C) 2017  Leandro Poli
#This program is free software; you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation; either version 3 of the License, or
#(at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301  USA

# Version: 1.0

import sys;
import re;

usage = '''Uso: cuit.py [LETRA SEXO] [DOCUMENTO]

Argumentos:

	LETRA SEXO:
			M: Masculino
			F: Femenino
			E: Empresa
	
	DOCUMENTO: 7 u 8 dígitos numéricos sin puntos''';
	
nroMasculino = 20;
nroFemenino = 27;
nroEmpresa = 30;
nroNuevoPersona = 23;
nroNuevoEmpresa = 33;
nroPersonaRepetida = 24;
nroEmpresaRepetida = 34;
digitoCambio = 10;

def obtenerCuit(letra, documento, repetido):
	retorno = "";
	if(re.match("^[0-9]{7,8}$",documento)):
		if(sys.argv[1]=="M"):
			if(repetido):
				digitos = nroPersonaRepetida;
			else:
				digitos = nroMasculino;
		elif(sys.argv[1]=="F"):
			if(repetido):
				digitos = nroPersonaRepetida;
			else:
				digitos = nroFemenino;
		elif(sys.argv[1]=="E"):
			if(repetido):
				digitos = nroEmpresaRepetida;
			else:
				digitos = nroEmpresa;
		digitoVerificador = obtenerDigitoVerificador(digitos,documento);
		if(digitoVerificador == 10):
			if(sys.argv[1]=="M" or sys.argv[1]=="F"):
				digitos = nroNuevoPersona;
			else:
				digitos = nroNuevoEmpresa;
		digitoVerificador = obtenerDigitoVerificador(digitos,documento);
		retorno = str(digitos)+"-"+str(documento)+"-"+str(digitoVerificador);
	else:
		retorno = "El número de documento ingresado no coincide en formato";
	return retorno;

def obtenerDigitoVerificador(digitos, documento):
	retorno = 0;
	cuitString = str(digitos);
	cuitInteger = 0;
	if(len(documento) == 7):
		cuitString += "0";
	cuitString += str(documento);
	base = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2];
	for i in range(10):
		retorno += int(cuitString[i]) * base[i];
	retorno = 11 - (retorno % 11);
	if retorno == 11:
		retorno = 0;
	return retorno;

#Chequea si no hay 3 argumentos, entonces imprime la ayuda
#argv[0]: nombre del script
#argv[1]: letra sexo
#argv[2]: número de documento
if(len(sys.argv) != 3 ):
	print(usage);
#Chequea que sólo se ingrese una letra de las posibles	
elif(not re.match("[MFE]{1}", sys.argv[1]) or len( sys.argv[1])!= 1):
	print("Debe ingresar una letra válida");
#Calcula el CUIT
else:
	print("CUIT:")
	print(obtenerCuit(sys.argv[1],sys.argv[2],False));
	print("CUIT alternativo:")
	print(obtenerCuit(sys.argv[1],sys.argv[2],True));
	

	
