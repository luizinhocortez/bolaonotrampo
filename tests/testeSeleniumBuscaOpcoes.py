# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import codecs
import json
from pprint import pformat as pf
empresas = u'''AES TIETE ENERGIA SA
AMBEV S.A.
AREZZO INDÚSTRIA E COMÉRCIO S.A.
ATACADÃO S.A.
AZUL S.A.
B2W - COMPANHIA DIGITAL
B3 S.A. - BRASIL, BOLSA, BALCÃO
BB SEGURIDADE PARTICIPAÇÕES S.A.
BCO BRADESCO S.A.
BCO BRASIL S.A.
BCO BTG PACTUAL S.A.
BCO ESTADO DO RIO GRANDE DO SUL S.A.
BCO SANTANDER (BRASIL) S.A.
BR MALLS PARTICIPACOES S.A.
BRADESPAR S.A.
BRASKEM S.A.
BRF S.A.
CCR S.A.
CENTRAIS ELET BRAS S.A. - ELETROBRAS
CESP - CIA ENERGETICA DE SAO PAULO
CIA BRASILEIRA DE DISTRIBUICAO
CIA ENERGETICA DE MINAS GERAIS - CEMIG
CIA HERING
CIA LOCAÇÃO DAS AMÉRICAS
CIA PARANAENSE DE ENERGIA - COPEL
CIA SANEAMENTO BASICO EST SAO PAULO
CIA SANEAMENTO DE MINAS GERAIS-COPASA MG
CIA SANEAMENTO DO PARANA - SANEPAR
CIA SIDERURGICA NACIONAL
CIELO S.A.
CONSTRUTORA TENDA S.A.
COSAN S.A.
CTEEP - CIA TRANSMISSÃO ENERGIA ELÉTRICA PAULISTA
CVC BRASIL OPERADORA E AGÊNCIA DE VIAGENS S.A.
CYRELA BRAZIL REALTY S.A.EMPREEND E PART
DURATEX S.A.
ECORODOVIAS INFRAESTRUTURA E LOGÍSTICA S.A.
EDP - ENERGIAS DO BRASIL S.A.
EMBRAER S.A.
ENAUTA PARTICIPAÇÕES S.A.
ENERGISA S.A.
ENEVA S.A
ENGIE BRASIL ENERGIA S.A.
EQUATORIAL ENERGIA S.A.
ESTACIO PARTICIPACOES S.A.
FLEURY S.A.
GERDAU S.A.
GOL LINHAS AEREAS INTELIGENTES S.A.
GRENDENE S.A.
HAPVIDA PARTICIPACOES E INVESTIMENTOS SA
HYPERA S.A.
IGUATEMI EMPRESA DE SHOPPING CENTERS S.A
IOCHPE MAXION S.A.
IRB - BRASIL RESSEGUROS S.A.
ISHARES BMFBOVESPA SMALL CAP FUNDO DE ÍNDICE
ISHARES IBOVESPA FUNDO DE ÍNDICE
ISHARES S&P 500 FDO INV COTAS FDO INDICE
IT NOW IBOVESPA FUNDO DE ÍNDICE
ITAU UNIBANCO HOLDING S.A.
ITAUSA INVESTIMENTOS ITAU S.A.
JBS S.A.
KLABIN S.A.
KROTON EDUCACIONAL S.A.
LIGHT S.A.
LINX S.A.
LOCALIZA RENT A CAR S.A.
LOJAS AMERICANAS S.A.
LOJAS RENNER S.A.
M.DIAS BRANCO S.A. IND COM DE ALIMENTOS
MAGAZINE LUIZA S.A.
MAHLE-METAL LEVE S.A.
MARCOPOLO S.A.
MARFRIG GLOBAL FOODS S.A.
METALURGICA GERDAU S.A.
MINERVA S.A.
MOVIDA PARTICIPACOES SA
MRV ENGENHARIA E PARTICIPACOES S.A.
MULTIPLAN - EMPREEND IMOBILIARIOS S.A.
NATURA COSMETICOS S.A.
NOTRE DAME INTERMEDICA PARTICIPACOES SA
ODONTOPREV S.A.
OI S.A.
PETROBRAS DISTRIBUIDORA S/A
PETROLEO BRASILEIRO S.A. PETROBRAS
QUALICORP CONSULTORIA E CORRETORA DE SEGUROS S.A.
RAIA DROGASIL S.A.
RANDON S.A. IMPLEMENTOS E PARTICIPACOES
RUMO S.A.
SANTOS BRASIL PARTICIPACOES S.A.
SMILES FIDELIDADE S.A.
SUL AMERICA S.A.
SUZANO S.A.
TELEFÔNICA BRASIL S.A
TIM PARTICIPACOES S.A.
TOTVS S.A.
TRANSMISSORA ALIANÇA DE ENERGIA ELÉTRICA S.A.
ULTRAPAR PARTICIPACOES S.A.
USINAS SID DE MINAS GERAIS S.A.-USIMINAS
VALE S.A.
VALID SOLUÇÕES S.A.
VIA VAREJO S.A.
WEG S.A.'''.split('\n')


def preencheElemento(elemId, value):
	elem = driver.find_element_by_xpath(elemId)
	elem.clear()
	elem.send_keys(value)

def enviaEnter(elemId):
	elem = driver.find_element_by_xpath(elemId)
	elem.send_keys(Keys.RETURN)

dados = list()
with codecs.open('dados.out', mode='a', encoding="utf-8") as the_file:
	driver = webdriver.PhantomJS(executable_path='D:/temp/tarefas/selenium/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs.exe')
	for k,nomeEmpresa in enumerate(empresas):
		driver.get("http://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/consultas/mercado-a-vista/opcoes/posicoes-em-aberto/")
		elem = driver.find_element_by_css_selector('#filtro > div > div > div:nth-child(1) > div > div > input[type="radio"]:nth-child(5)')
		elem.click()
		elem = driver.find_element_by_css_selector('#dataVencimento > option:nth-child(1)')
		elem.click()
		preencheElemento('//*[@id="nomeEmpresa"]',nomeEmpresa)
		print 'consultando empresa %s %s' % (k,nomeEmpresa)
		elem = driver.find_element_by_xpath("/html/body/div[5]/div/div/div[3]/div[2]/div/div/div[2]/button")
		elem.click()
		elem = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/div/div[1]/table/tbody/tr/td/a')
		elem.click()
		driver.save_screenshot('%s.png' % nomeEmpresa)
		tabela = driver.find_element_by_css_selector('body > div.bg-conteudo > div > div > div.small-12.small-pull-12.medium-9.medium-pull-3.large-9.large-pull-3.columns')
		for l in tabela.text.split('\n'):
			dados.append(l)
			the_file.write(l)
			the_file.write('\n')

# debug cortez ate aqui	

