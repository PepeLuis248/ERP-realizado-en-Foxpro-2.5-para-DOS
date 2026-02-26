*  Programa: FER110.PRG
* Comentario: Modulo de I.V.A. ventas/compras.
* Manejo de errores
on error do error with sys(16)
* Aborta por ejecucion individual de este programa
if sys(16) = sys(16,1)
   cancel
endif
* Controla nro/serie de lenguaje/base
do nuc002
dimension mes(12)
mes(01) = "ENERO"
mes(02) = "FEBRERO"
mes(03) = "MARZO"
mes(04) = "ABRIL"
mes(05) = "MAYO"
mes(06) = "JUNIO"
mes(07) = "JULIO"
mes(08) = "AGOSTO"
mes(09) = "SEPTIEMBRE"
mes(10) = "OCTUBRE"
mes(11) = "NOVIEMBRE"
mes(12) = "DICIEMBRE"
store 0 to x_mes, x_ano
do while .t.
   set color to w/n
   @  3, 0 , 21,79 box ' '
   set color to w/n+
   @  4,31 fill to 6,52 color n/n+
   @  3,29 , 5,50 box ' '
   @  3,36 say " Modulo "
   @  4,32 prompt "Ventas"
   @  4,41 prompt "Compras"
   opc = 1
   menu to opc
   do case
      case opc = 0
           close databases
           exit
      case opc = 1  && Trabaja con datos de iva/ventas
           oriaux = "V"
      case opc = 2  && Trabaja con datos de iva/compras
           oriaux = "C"
   endcase
   set color to w/n+
   @  9,10 fill to 13,32 color n/n+
   @  8, 8 , 12,30 box ' '
   @  8,15 say " Opciones "
   @  9, 9 prompt "Genera libro contable"
   @ 10, 9 prompt "Acumulados en periodo"
   @ 11, 9 prompt "Grafico de progresion"
   opc = 1
   menu to opc
   if opc = 0
      loop
   endif
   do case
      case opc = 1
           tit = "Emision de libro iva/"
           do pide with  8, 35, tit
      case opc = 2
           tit = "Acumulados sobre "
           do pide with  8, 35, tit
      case opc = 3
           tit = "Progresion de iva/"
   endcase
   tit = tit + iif(oriaux = "V", "ventas", "compras")
   if lastkey() = 27
      loop
   endif
   do case
      case opc = 1     && Genera libro
           do fer111 with oriaux
      case opc = 2     && Acumula por periodo
           do fer112 with oriaux
      case opc = 3     && Grafico de progresion de iva
           do fer113 with oriaux
   endcase
enddo
* Procedimiento: Pide
*    Comentario: Acepta mes y ano para proceso posterior.
procedure pide
parameters fil, col, tit
@ fil+1,col+2 fill to fil+6,col+43 color n/n+
set color to w/n+
@ fil,col , fil+5,col+41 box ' '
set color to n/w
@ fil+1,col+1 say space(40)
@ fil+1,(col+20)-(len(tit)/2) say tit
set color to w/n+
@ fil+3,col+2 say "Indique mes..."
@ fil+4,col+2 say "Indique ano..."
set color to w/n
store 0 to x_mes, x_ano
orden = 1
do while .t.
   do case
      case orden = 1
           @ fil+3,col+17 say space(15)
           @ fil+3,col+17 get x_mes function "@B 99" range 1,12
           read
           if lastkey() = 27
              exit
           endif
           if .not. empty(x_mes)
              @ fil+3,col+17 say mes(x_mes)
           endif
      case orden = 2
           @ fil+4,col+17 say space(15)
           @ fil+4,col+17 get x_ano function "@B 9999"
           read
           @ fil+4,col+17 say padl(x_ano, 4, "0")
           if lastkey() = 27
              exit
           endif
           if .not. between(x_ano, 0, 9999)
              ?? chr(7)
              loop
           endif
           if readkey() <> 4
              exit
           endif
   endcase
   if readkey() = 4
      if orden > 1
         orden= orden-1
      endif
   else
      if orden < 2
         orden= orden+1
      endif
   endif
enddo
* End/fer110.PRG
