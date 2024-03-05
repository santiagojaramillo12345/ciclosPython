def Multiplicar():
    nro = int(input("digite un numero"))
    for i in range(11):
        print(f"{i}*{nro} = {i*nro}")


   #digitar la nota final de un grupo y contar cuantos ganan y cuantos pierden el promedio


    if __name__=='__main__':
        Multiplicar()

        print("registro de notas**".center(50,"_"))
        N= int(input("cantiadad de estudiante"))
        print("".center(30,"_"))

        #simpre hay que iniciar la cantidad  y acum
        contGano=0
        contPerdio =0
        acumNota=0

        for i in range(n):
            nota=float("nota final ->")
            if nota>=3:
                contGano +=1
            else:
                contPerdio +=1
            acumNota +=nota
            print(contPerdio)


    promedio= acumNota /N
    print("".center(50,"_"))
    print('** INFORME ACADEMICO **'.center(50," "))
    print(f"numero de estudiantes perdieron ->{contPerdio}")
    print(f"numero de estudiantes ganaron --->{contGano}")
    print(f"promedio de grupo --------------->{promedio}")

 