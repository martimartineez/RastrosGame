

# El juego comienza aquí.
label start:

    scene blanco with dissolve
    play music "principio.mp3" loop
    "No podría decir en qué momento empezó a llamar mi atención, lo hizo de forma silenciosa y progresiva."
    "Al principio solo inclinaba la mirada, quizá desaceleraba el paso, de reojo espiaba alguna ventana o seguía las líneas de los encajes."
    "Presentía que tarde o temprano me sería imposible seguir de largo, posponer un día más lo inevitable."
label escena1:
    scene afuera with dissolve
    "Hoy finalmente me detengo. La observo frente a mí, llana y polvorienta, ¿por qué es distinta a las otras? Hay tantas así en el barrio, abandonadas."
    "Pareciera llamarme, oculta detrás de una máscara. La calle desierta, el mediodía soleado, algo que me impide volver a rechazarla. Decido finalmente {color=62A9FF}adentrarme. {/color}"
    $ result = renpy.imagemap ("afuera.jpg", "afuera1.png", [(650, 55, 1050, 1000, "a")])
    if result == "a":
        play sound "puerta.mp3"
        jump escena2

label escena2:
    stop music
    play music "ambiente.mp3" loop
    scene recibidor with dissolve
    "Se siente tan extraño dejar atrás el día y sumergirse en la penumbra del recibidor. Alcanzo a ver los restos, las huellas de lo que alguna vez habrá sido la entrada a un hogar."
    "Por alguna razón me parecen inmensos, todo se alza interminable frente a mí. "
    "Tanto tiempo preguntándome cómo sería de este lado, y ahora tengo la posibilidad de ver, escuchar y hasta de palpar…"
    "¿Qué es esta fascinación tan envolvente?  Mis manos se mueven solas. "
    "Trato de {color=FF9331}alcanzar{/color} un pequeño espejo…"
    $ result = renpy.imagemap ("recibidor.png", "recibidor1.png", [(425, 470, 670, 730, "a")])
    if result =="a":
        jump escena3
label escena3:
    scene recibidor2 with dissolve
    $ result = renpy.imagemap ("recibidor2.png", "recibidor3.png" , [(255, 250, 855, 780, "a")])
    if result =="a":
        play sound "espejo.mp3"
        jump escena4

label escena4:
    scene recibidor4 with dissolve
    "Pero el clavo ya no resiste. Debería ser más cuidadoso, no quiero meterme en problemas."
    play sound "relojrotolejos.mp3" loop
    "Un ruido pesado y monótono llega flotando a través de la puerta, me pregunto de dónde viene."
    jump escena5

label escena5:
    scene blanco with dissolve
    "Quizá debería irme…"
    stop sound
    jump escena6

label escena6:
    scene comedor with dissolve
    play sound "relojrotocerca.mp3" loop
    "El origen del ruido es aquel enorme reloj en mitad del salón. Está estropeado y ya no corre. Qué extraño es este lugar, no solo me parece inmenso, hay algo más."
    "No hay dudas de que éste es el comedor. A pesar de que la casa lleva abandonada muchos años, el mantel, los cubiertos… todo sigue ahí, intacto, como en una fotografía. "
    "De un momento a otro podrían venir y sentarse a almorzar, como cualquier domingo. Entonces, ¿por qué no? ¿Qué pasaría…? "
    "Qué molesto me resulta ese reloj. Quizá, si pudiera {color=B05F3C}arreglarlo…{/color}"
    $ result = renpy.imagemap ("comedor.jpg", "comedor1.png", [(1225, 100, 1450, 225, "a")])
    if result =="a":
        stop sound
        play sound "reloj_arreglado.mp3"
        "Qué alivio, no sé por qué retumbaba tanto. Me pregunto si los dormitorios también seguirán intactos…"
        jump escena7
label escena7:
    scene blanco with dissolve
    play sound "escaleras.mp3"
    "Estos escalones también parecen gigantes, y muy viejos, espero resistan mi peso"
    jump escena8

label escena8:
    stop sound
    scene padres with dissolve
    "Aunque no haya nadie, es incómodo entrar a escondidas a un dormitorio."
    "Sé que suena un poco infantil, al fin y al cabo soy un intruso desde que crucé el umbral a la calle, pero a pesar del tiempo, la atmósfera íntima sigue pegada a estos cuartos. "
    "Parecería haber sido vaciado de golpe. ¿Y si sufrieron un robo? Mi papá solía decir que el barrio no era seguro, que entraban a robar todo el tiempo."
    "Incluso una vez trajo algo a la casa, “para proteger a la familia”."
    "La sensación de que no debería estar acá se hace más fuerte."
    "Voy a tratar de irme lo antes posible, solo quiero saber si ellos también tenían algo para protegerse. Quizá, en alguno de estos {color=666699}cajones…{/color}"
    $ result = renpy.imagemap ("padres.jpg", "padres1.png", [(1400, 400, 1650, 650, "a")])
    if result =="a":
        jump escena77
label escena77:
    scene padres2 with dissolve
    play sound "arma.mp3"
    "Lo suponía, se ve que mi papá tenía razón sobre el barrio."
    "Mi mamá al principio no quería saber nada, después entendió que era por el bien de los tres."
    "Lo mejor es que no la toque, hay otro dormitorio al final del pasillo."
    jump escena9

label escena9:
    scene blanco with dissolve
    "Cuanto más me adentro en la casa, mayor es mi curiosidad. Debería haberlo hecho antes"
    jump escena10

label escena10:
    scene chicos with dissolve
    "Este cuarto es el que más me gusta hasta ahora, el otro me hacía sentir muy incómodo. "
    "¿Por qué el tiempo actúa de forma tan dispareja en esta casa? Quizá éste también sea su cuarto favorito. "
    "Las paredes todavía desprenden un eco de juegos y risas."
    "Si pudiera saber algo sobre ellos… debería prestar más atención, aunque me cuesta mucho concentrarme desde que entré."
    "Me disperso con facilidad y termino en cualquier lugar, como cuando era chico. "
    "Creo que hay algo escondido bajo la cama, al final de esos coloridos {color=CC9900}lis{/color}{color=FF3300}to{/color}{color=003399}nes…{/color}"
    $ result = renpy.imagemap ("chicos.jpg", "chicos1.png", [(615, 650, 845, 825, "a")])
    if result =="a":
        jump escena01
label escena01:
    play sound "listones.mp3"
    scene chicos2 with dissolve
    "De a dos seguro era fácil pasar el rato. Yo me aburría mucho, me hubiera gustado tener un hermano. "
    "Quizá así recordaría alguna tarde de juegos. "
    jump escena11

label escena11:
    scene blanco with dissolve
    "Mi única compañía era un pajarito que mamá había traído de un refugio."
    "Se llamaba… ¿Cómo se llamaba? "
    jump escena12

label escena12:
    scene jardin1 with dissolve
    "{color=FF0000}Manuel.{/color} Ese era su nombre."
    "Le gustaba ir de un lado al otro, nunca se quedaba quieto."
    $ result = renpy.imagemap ("jardin1.png", "jardin1a.png", [(1300, 95, 1550, 400, "a")])
    if result =="a":
        play sound "aleteo1.mp3"
        jump escena02
label escena02:
    scene jardin2 with dissolve
    "Solo descansaba cuando llegaba la hora de la merienda, entonces jugábamos a las cartas"
    $ result = renpy.imagemap ("jardin2.png", "jardin2a.png", [(200, 135, 540, 470, "a")])
    if result =="a":
        play sound "aleteo2.mp3"
        jump escena03
label escena03:
    scene jardin3 with dissolve
    "Siempre estábamos juntos, él se la pasaba silbando mientras yo hacía dibujos o veíamos algún partido en la televisión."
    "A veces charlábamos de superhéroes o salíamos al jardín a cortar flores."
    $ result = renpy.imagemap ("jardin3.png", "jardin3a.png", [(200, 0, 850, 375, "a")])
    if result =="a":
        play sound "aleteo3.mp3"
        jump escena04
label escena04:
    scene jardin4 with dissolve
    "Íbamos por toda la casa buscando lugares nuevos para escondernos… "
    "hasta que se hizo más grande y ya no quería salir de su jaula. "
    $ result = renpy.imagemap ("jardin4.png", "jardin4a.png", [(850, 150, 1000, 450, "a")])
    if result =="a":
        jump escena13

label escena13:
    scene blanco with dissolve
    "Silbaba cada vez menos, y ya no volaba por el jardín, pero nunca me dejaba solo."
    "Y yo nunca lo dejaba solo a él, mamá y papá se ponían muy contentos cuando nos veían jugar juntos, aunque era inevitable que peleáramos cada tanto, siempre es así… "
    "Otra vez estoy pensando en cualquier cosa, podría quedarme todo el día divagando y aunque se hiciera de noche creo que no me daría cuenta. "
    play sound "ladrones.mp3"
    "De pronto el eco de un {color=666699}ruido metálico{/color} hace que me despabile y sienta un aire frío en el estómago."
    "¿Será que hay alguien más en la casa? Me acuerdo del día en que estaba en mi cuarto y también escuché un ruido muy parecido, desde la cocina…"
    jump escena14

label escena14:
    scene cocina with dissolve
    "Llegué y vi la jaula vacía."
    "No entendía lo que estaba pasando hasta que vi las plumas en el piso y me acordé de lo que papá solía decir, acerca del barrio. "
    "Los llamé a los dos pero ninguno me contestó, no eran ellos los que habían abierto la jaula. "
    "Me costaba asimilarlo, no era como en las películas, todo seguía en silencio pero algo no estaba bien."
    "El temor me paralizaba y me negaba a reconocer eso que ya sabía, quizá en ese momento tendría que haber mirado hacia otro lado, hacer de cuenta que no pasaba nada, pero no pude. "
    "“Ladrones” pensé al fin, “Quieren llevarse a Manuel”."
    "El {color=CC0033}rastro de plumas{/color} me indicaba el camino, solo tenía que seguirlo."
    $ result = renpy.imagemap ("cocina.jpg", "cocina1.png", [(1050, 550, 1150, 645, "a")])
    if result =="a":
        play sound "plumas.mp3"
        jump escena05
label escena05:
    scene cocina
    $ result = renpy.imagemap ("cocina.jpg", "cocina2.png", [(1300, 540, 1400, 645, "a")])
    if result =="a":
        play sound "plumas.mp3"
        jump escena15

label escena15:
    scene blanco with dissolve
    "Corrí a la habitación de mis papás sin pensar lo que hacía."
    play sound "seguro.mp3"
    "Abrí el cajón y ahí estaba. Helada y rígida, como esperándome."
    "Tuve que tomarla con ambas manos, era mucho más pesada de lo que parecía."
    "Sentí un vuelco en el estómago, pensé en ese instante que aunque mamá no estuviera de acuerdo, papá había hecho bien en traerla, teníamos que protegernos de alguna forma. "
    jump escena16

label escena16:
    scene pasillo with dissolve
    "El rastro se extendía por todo el pasillo y llevaba directo al jardín."
    "Solo podía pensar en lo que pasaría si me veían, o si decidían volver a entrar a la casa. "
    "Nunca me pregunté por qué se lo llevaban, o cómo habían entrado sin hacer ruido. "
    "Me aterraba la idea de quedarme solo y a la vez, si lo salvaba, si podía defender nuestra casa, lo orgullosos que estarían de mí. "
    "Mamá y papá amaban a Manuel, tanto como a mí. "
    "Me aferré al metal con decisión y corrí hacia el {color=660099}fondo.{/color} "
    "“Quieren escaparse por el techo”, pensé. No podía dejar que se lo llevaran."
    "Manuel era mi única compañía."
    $ result = renpy.imagemap ("pasillo.jpg", "pasillo1.png", [(1000, 50, 1400, 460, "a")])
    if result =="a":
        play sound "ventanal.mp3"
        jump escena17

label escena17:
    scene jardinfinal with dissolve
    "Vi la silueta del ladrón escabulléndose entre las flores, al final del rastro que desprendía Manuel, incapaz de soltarse o gritar."
    "{color=FF0000}Apunté{/color} directo hacia {color=FF0000}él{/color}, como me había enseñado mi papá…"
    stop music
    "Y sentí que hasta mis huesos se estremecían cada vez que {color=FF0000}presionaba…{/color}"
    $ result = renpy.imagemap ("jardinfinal.jpg", "jardinfinala.png", [(850, 400, 1000, 720, "a")])
    if result =="a":
        play sound "disparo.mp3"
        jump escena07
label escena07:
    scene jardinfinal1
    $ result = renpy.imagemap ("jardinfinal1.png", "jardinfinal1a.png", [(850, 400, 1000, 720, "a")])
    if result =="a":
        play sound "disparo.mp3"
        jump escena08
label escena08:
    scene jardinfinal2
    $ result = renpy.imagemap ("jardinfinal2.png", "jardinfinal2a.png", [(850, 400, 1000, 720, "a")])
    if result =="a":
        play sound "disparo.mp3"
        jump escena09
label escena09:
    scene jardinfinal3
    $ result = renpy.imagemap ("jardinfinal3.png", "jardinfinal3a.png", [(850, 400, 1000, 720, "a")])
    if result =="a":
        jump escena18
label escena18:
    scene jardinfinal3
    "El eco de las explosiones se apagó, volvió la calma del día y era como si nada hubiese pasado. "
    play music "final.mp3"
    "Junto al cuerpo de Manuel alcancé a ver un pequeño pozo, del tamaño de un pájaro, la tierra recién extraída."
    "Mis papás lo habían oído todo desde el comedor y salieron desesperados al jardín."
    "Mamá gritaba una y otra vez, “Manuel, Manuel” y yo no sabía cómo decirle que ya era tarde, que no había podido salvarlo del ladrón. "
    "Mi papá llegó de golpe y me arrancó de un tirón aquel peso metálico de las manos."
    "Mientras yo me desplomaba de rodillas sobre el pasto y trataba de balbucear que no había llegado a tiempo. "
    "Le gritaba a mamá, pero ella prefería aferrarse al cuerpo del ladrón y me miraba, me miraba de una forma… ojalá nunca me hubiera mirado así."
    "Como si le hubieran arrancado una parte de su alma, como si me hubieran disparado a mí."
    "Mi papá me sacudía y me gritaba pero de su boca no salía nada, ni un sonido. Yo no sabía cómo explicarles, no entendía por qué me culpaban. "
    jump escena19
label escena19:
    scene muerte with dissolve
    jump fin

label fin:
    scene muerte
    "Yo solo quería protegernos, sobre todo a Manuel. Nunca le habría hecho daño a Manuel, pero ella me miraba de una forma…"
    "     FIN.   "

    # TERMINA EL JUEGO

    return
