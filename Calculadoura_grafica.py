from tkinter import *

valor = []
i = 0
control = 0
valor_real = [""]
resultado = 0
control2 = 0
operacao = []



app_calculadoura = Tk()
app_calculadoura.geometry("400x500+500+50")
app_calculadoura.title("Calculadoura Gráfica")

calculado = Frame(app_calculadoura,width = 400,height = 155,bd = 1,bg = "grey")
calculado.pack(side = TOP)


calculado1 = Label(calculado,width = 17,height = 3,bd = 0,bg= "grey")
calculado1.place(x=0,y=0)



def mostra_numero(button_id):
    global i
    global control
    global resultado
    global control2
    global operacao


    if button_id == 0:
        
        valor.append("0")
        calculado1["font"] = 'ariel',30,'bold'
        
    elif button_id == 1:
        
        valor.append("1")
        calculado1["font"] = 'ariel',30,'bold'
        
    elif button_id == 2:
        
        valor.append("2")
        calculado1["font"] = 'ariel',30,'bold'

    elif button_id == 3:
        
        valor.append("3")
        calculado1["font"] = 'ariel',30,'bold'

    elif button_id == 4:
        
        valor.append("4")
        calculado1["font"] = 'ariel',30,'bold'

    elif button_id == 5:
        
        valor.append("5")
        calculado1["font"] = 'ariel',30,'bold'

    elif button_id == 6:
        
        valor.append("6")
        calculado1["font"] = 'ariel',30,'bold'


    elif button_id == 7:
        
        valor.append("7")
        calculado1["font"] = 'ariel',30,'bold'

    elif button_id == 8:
        
        valor.append("8")
        calculado1["font"] = 'ariel',30,'bold'


    elif button_id == 9:
        
        valor.append("9")
        calculado1["font"] = 'ariel',30,'bold'

    elif button_id == "+":
        
        valor.append("+")
        calculado1["font"] = 'ariel',30,'bold'

    elif button_id == "-":
        
        valor.append("-")
        calculado1["font"] = 'ariel',30,'bold'

    elif button_id == "X":
        
        valor.append("x")
        calculado1["font"] = 'ariel',30,'bold'

    elif button_id == "/":
        
        valor.append("/")
        calculado1["font"] = 'ariel',30,'bold'

    elif button_id == ".":
        
        valor.append(".")
        calculado1["font"] = 'ariel',30,'bold'

    elif button_id == "%":

        valor.append("%")
        control = 1 

    elif button_id == "igual":

        control = 1
 
        
    if control != 1:
        calculado1["text"] = calculado1["text"] + valor[i]
        i += 1
    else:
        for junt in range (len(valor)):
            if valor[junt] != "+" and valor[junt] != "-" and valor[junt] != "x" and valor[junt] != "/" and valor[junt] != "%" :
                valor_real[control2] = valor_real[control2] + valor[junt]
            else:
                if valor[junt] == "+":
                    operacao.append("+")

                elif valor[junt] == "-":
                    operacao.append("-")

                elif valor[junt] == "x":
                    operacao.append("x")
                    
                    
                elif valor[junt] == "/":
                    operacao.append("/")

                else:
                    operacao.append("%")


                control2 += 1
                valor_real.append("")



        for I in valor_real:
            for I2 in operacao:
                if I2 == "+":
                    resultado = resultado + float(I)
                    break
                elif I2 == "-":
                    if resultado == 0:
                        resultado = float(I)
                        break
                    else:
                        resultado = resultado - float(I)
                        break
                    
                elif I2 == "x":
                    if resultado == 0:
                        resultado = 1
                    resultado = resultado*float(I)
                    break
                
                elif I2 == "/":
                    if resultado == 0:
                        resultado = float(I)
                        break
                    else:
                        resultado = resultado/float(I)
                        break
                elif I2 == "%":
                    del valor_real[-1]
                    resultado = float(I)/100
                    break
                    
                        
                


        calculado1["text"] = resultado


    
def bt_apaga(buttun_ok2):
    global i
    global control
    global resultado
    global control2
    global operacao

    if buttun_ok2 == "C":
        del valor[:]
        del valor_real[:]
        valor_real.append("")
        del operacao[:]
        control = 0
        resultado = 0
        control2 = 0
        i = 0
        calculado1["text"] = ""

    if buttun_ok2 == "<-":
        i = i-1
        del valor[-1]
        calculado1["text"] = calculado1["text"][:-1]
        


        
bt_converte = Button(app_calculadoura,width = 8,height = 3,font =('ariel',14,'bold') ,text = "+/-", command = lambda: mostra_numero("+/-"))
bt_converte.place(x=0,y=430)


bt_0 = Button(app_calculadoura,width = 8,height = 3 ,font =('ariel',14,'bold'),text = "0", command = lambda: mostra_numero(0))
bt_0.place(x=101,y=430)


bt_ponto = Button(app_calculadoura,width = 8,height = 3 ,font =('ariel',14,'bold'),text = ".", command = lambda: mostra_numero("."))
bt_ponto.place(x=205,y=430)


bt_igual = Button(app_calculadoura,width = 7,height = 3 ,font =('ariel',14,'bold'),text = "=", command = lambda: mostra_numero("igual"))
bt_igual.place(x=308,y=430)


bt_1 = Button(app_calculadoura,width = 8,height =3 ,font =('ariel',14,'bold'),text = "1", command = lambda: mostra_numero(1))
bt_1.place(x=0,y=355)

bt_2 = Button(app_calculadoura,width = 8,height = 3 ,font =('ariel',14,'bold'),text = "2", command = lambda: mostra_numero(2))
bt_2.place(x=101,y=355)


bt_3 = Button(app_calculadoura,width = 8,height = 3 ,font =('ariel',14,'bold'),text = "3", command = lambda: mostra_numero(3))
bt_3.place(x=205,y=355)

bt_mais = Button(app_calculadoura,width = 7,height = 3 ,font =('ariel',14,'bold'),text = "+", command = lambda: mostra_numero("+"))
bt_mais.place(x=308,y=355)


bt_4 = Button(app_calculadoura,width = 8,height = 3 ,font =('ariel',14,'bold'),text = "4", command = lambda: mostra_numero(4))
bt_4.place(x=0,y=290)


bt_5 = Button(app_calculadoura,width = 8,height = 3 ,font =('ariel',14,'bold'),text = "5", command = lambda: mostra_numero(5))
bt_5.place(x=101,y=290)


bt_6 = Button(app_calculadoura,width = 8,height = 3 ,font =('ariel',14,'bold'),text = "6", command = lambda: mostra_numero(6))
bt_6.place(x=205,y=290)


bt_menos = Button(app_calculadoura,width = 7,height = 3 ,font =('ariel',14,'bold'),text = "-", command = lambda: mostra_numero("-"))
bt_menos.place(x=308,y=290)


bt_7 = Button(app_calculadoura,width = 8,height = 3 ,font =('ariel',14,'bold'),text = "7", command = lambda: mostra_numero(7))
bt_7.place(x=0,y=225)


bt_8 = Button(app_calculadoura,width = 8,height = 3 ,font =('ariel',14,'bold'),text = "8", command = lambda: mostra_numero(8))
bt_8.place(x=101,y=225)


bt_9 = Button(app_calculadoura,width = 8,height = 3 ,font =('ariel',14,'bold'),text = "9", command = lambda: mostra_numero(9))
bt_9.place(x=205,y=225)


bt_mult = Button(app_calculadoura,width = 7,height = 3 ,font =('ariel',14,'bold'),text = "X", command = lambda: mostra_numero("X"))
bt_mult.place(x=308,y=225)


bt_limpar_tudo = Button(app_calculadoura,width = 8,height = 3 ,font =('ariel',14,'bold'),text = "C", command = lambda: bt_apaga("C"))
bt_limpar_tudo.place(x=0,y=155)


bt_limpar = Button(app_calculadoura,width = 8,height = 3 ,font =('ariel',14,'bold'),text = "<-", command = lambda: bt_apaga("<-"))
bt_limpar.place(x=101,y=155)


bt_porcent = Button(app_calculadoura,width = 8,height = 3 ,font =('ariel',14,'bold'),text = "%", command = lambda: mostra_numero("%"))
bt_porcent.place(x=205,y=155)


bt_div = Button(app_calculadoura,width = 7,height = 3 ,font =('ariel',14,'bold'),text = "/", command = lambda: mostra_numero("/"))
bt_div.place(x=308,y=155)


app_calculadoura.mainloop()

