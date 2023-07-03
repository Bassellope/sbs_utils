from sbs_utils.mast.mast import Mast
from sbs_utils.mast.mastsbs import MastSbs
import unittest

Mast.enable_logging()

"""
    Target,
    Tell,
    Comms,
    Button,
    Near,
    Simulation
"""

def mast_sbs_compile(code):
    mast = MastSbs()
    errors = mast.compile(code)
    return (errors, mast)


class TestMastSbsCompile(unittest.TestCase):
    
    
    def test_compile_no_err(self):
        (errors, mast) = mast_sbs_compile( code = """
transmit player self "Hello"
receive  player self "Hello" 

have self broadcast "Hello, World"
have self broadcast "Hello, RGB" color "#fff"




await self comms player:
    * "Button one":
        -> JumpLabel
    + "Button Two":
        -> JumpLabel
    + "Button Jump":
timeout 1m 1s:
        -> JumpSomeWhere
end_await


await self comms player:
* "Button one":
    await self comms player:
    * "Button one":
        await self comms player:
        * "Button one":
            -> JumpLabel
        end_await
    end_await
end_await


""")
        if len(errors)>0:
            for err in errors:
                print(err)
        assert(len(errors) == 0)

     
    def test_compile_no_err_2(self):
        (errors, mast) = mast_sbs_compile( code ="""
# Set the comms buttons to start the 'quest'

await self comms player:
+ "Start at DS1":
 -> One
+ "Start at DS2":
 -> Two
+ "Taunt":
 -> Taunt
 end_await


== Taunt ==

await self comms player:
    * "Your mother"  color "red":
        -> Taunt
    + "Kiss my Engine"  color "green":
        -> Taunt
    + "Skip me" color "white" if x > 54:
        -> Taunt 
    * "Don't Skip me" color "white" if x < 54:
     -> Taunt 
    + "Taunt" :
        -> Taunt
end_await


== One ==
await=>HeadToDS1
await=>HeadToDS2
->One

== Two ==
await=>HeadToDS2
await=>HeadToDS1
->Two

== Start ==

await self comms player:
+ "Say Hello" :
-> Hello
+ "Say Hi":
 -> Hi
+ "Shutup":
 -> Shutup
end_await


== skip ==
receive player self "Come to pick the princess"
== Hello ==
transmit self player  "HELLO"

await self comms player:
+ "Say Blue":
-> Blue
+ "Say Yellow":
-> Yellow
+ "Say Cyan":
-> Cyan
end_await


== Hi ==
receive self player  "Hi"
delay 10s
-> Start

== Chat ==
receive self player  "Blah, Blah"
delay 2s
-> Chat

== Shutup ==
cancel chat

== Blue ==
receive self player  "Blue"
delay 10s
-> Start

== Yellow ==
receive self player  "Yellow"
delay 10s
-> Start

== Cyan ==
receive self player  "Cyan"
await self comms player timeout 5s:
+ "Say main":
    -> main
timeout:
-> TooSlow
end_await


== TooSlow ==
receive self player  "Woh too slow"
delay 10s
-> Start

""")
        if len(errors)>0:
            for err in errors:
                print(err)
        assert(len(errors) == 0)



    def test_scan_compile_no_err(self):
        (errors, mast) = mast_sbs_compile( code ="""
=========== server_main =====
await artemis scan raider1:
    scan tab "scan":
        scan results "test"
end_await

await artemis scan raider1:
    scantab "scan":
        scan results "This space object is now scanned, in the most general way. This text was generated by the script."
    scan tab "bio":
        scan results "This space object has indeterminate life signs. This text was generated by the script."
    scan tab "intel":
        scan results "This space object is detailed in the ship's computer banks. This text was generated by the script."
    scan tab "sgnl":
        scan results "This space object radiating signals. This text was generated by the script."
end_await

->END


""")
        if len(errors)>0:
            for err in errors:
                print(err)
        assert(len(errors) == 0)





#     def test_run_tell_no_err(self):
#         (errors, runner, mast) = mast_sbs_run( code = """
#  have self tell player "Hello"
#  have self tell player "Hello" color "black"
# """)
#         if len(errors)>0:
#             for err in errors:
#                 print(err)
#         assert(len(errors) == 0)


"""
--------await self near player 700 timeout 1m 1s:----------

----------timeout:-----------------

----------end_await-----------------


await self comms player timeout 1m 1s:
* "Button one": ******

+ "Button Two":
-> JumpLabel
+ "Button Jump": 
+ "Button Push":
->> PushLabel
+ "Button Pop":
<<-
+ "Button Await 1": ****
    await => par
++++++++++++ "Button Await 1":  ****
await => par {"S":1}
+++++++++++ "Button Await 1": ******
await => par ~~ {
    "S":1
    }~~
------------- timeout:---------------
-> JumpSomeWhere
---------------end_await ----------------
"""

    
if __name__ == '__main__':
    try:
        unittest.main(exit=False)
    except Exception as e:
        print(e.msg)

