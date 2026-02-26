* Pantalla: fer000.PRG
set talk off
set bell off
set date french
set delete on
set escape off
on key = 302 do calcu
* Manejo de errores
on error do error with sys(16)
* Aborta por ejecucion individual de este programa
if sys(16) = sys(16,1)
   cancel
endif
* Controla nro/serie de lenguaje/base
do nuc002
public spool, comercio, detalle
select 10
use indices
comercio = razind
spool    = ltrim(rtrim(dirspolind))
set procedure to fer099.prg
save screen to pan_yyy
do while .t.
   restore screen from pan_yyy
   set exclusive off
   close databases
   do pan000
   set color to w/n+
   @ 22, 0 , 22,79 box ' '
   do case
      case opc = 0 && Salida
           exit
      case opc =  1 && Gestion de Clientes
           do fer001
      case opc =  2 && Gestion de Proveedores
           do fer002
      case opc =  3 && Gestion de vendedores
           if jerarquia < 3
              save screen to pan_conf
              set color to w/n+
              @ 21,28 , 23,50 box ' '
              set color to w/n
              @ 22,29 say 'Usuario no autorizado'
              ? chr(7)
              close databases
              ESPERA=inkey(0)
              restore screen from pan_conf
              select 10
              use auditor
              append blank
              replace ideusu with usuario
              replace fecusu with date()
              replace horusu with time(1)
              replace detusu with "Intento utilizar modulo de vendedores"
              use
              return
           endif
           do fer700
      case opc =  4 && Gestion de depositos
           do fer030
      case opc =  5 && Gestion de Tarjetas
           if jerarquia < 3
              save screen to pan_conf
              set color to w/n+
              @ 21,28 , 23,50 box ' '
              set color to w/n
              @ 22,29 say 'Usuario no autorizado'
              ? chr(7)
              close databases
              ESPERA=inkey(0)
              restore screen from pan_conf
              select 10
              use auditor
              append blank
              replace ideusu with usuario
              replace fecusu with date()
              replace horusu with time(1)
              replace detusu with "Intento utilizar modulo tarjetas/credito"
              use
              return
           endif
           do fer003
      case opc =  6 && Gestion de Articulos
           do fer004
      case opc =  7 && Control de Existencias
           do fer005
      case opc =  8 && Gestion de Compras
           do fer006
      case opc =  9 && Gestion de Ventas
           do fer007
      case opc = 10 && Precios
           do fer008
      case opc = 11 && Ofertas
           do fer009
      case opc = 12 && Control de Caja
           do fer100
      case opc = 13 && Listado mayor de cuentas
           do may000
      case opc = 14 && Liquidacion de I.V.A.
           if jerarquia < 3
              save screen to pan_conf
              set color to w/n+
              @ 21,28 , 23,50 box ' '
              set color to w/n
              @ 22,29 say 'Usuario no autorizado'
              ? chr(7)
              close databases
              ESPERA=inkey(0)
              restore screen from pan_conf
              select 10
              use auditor
              append blank
              replace ideusu with usuario
              replace fecusu with date()
              replace horusu with time(1)
              replace detusu with "Intento ingresar liquidaciones/IVA"
              use
              loop
           endif
           do fer110
      case opc = 15 && Estadisticas
           do fer120
      case opc = 16 && Auditorias de operaciones
           if jerarquia < 3
              save screen to pan_conf
              set color to w/n+
              @ 21,28 , 23,50 box ' '
              set color to w/n
              @ 22,29 say 'Usuario no autorizado'
              ? chr(7)
              close databases
              ESPERA=inkey(0)
              restore screen from pan_conf
              select 10
              use auditor
              append blank
              replace ideusu with usuario
              replace fecusu with date()
              replace horusu with time(1)
              replace detusu with "Intento consultar auditorias/operaciones"
              use
              loop
           endif
           do fer130
      case opc = 17 && Cuentas Corrientes
           do fer140
   endcase
enddo
close databases
set color to w/n
* End/fer000.PRG
