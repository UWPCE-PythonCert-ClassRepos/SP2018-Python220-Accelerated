# coroutines

async def corout():
    print("running corout")
    return "something returned"

#note that the returned value gets tacked on to the StopIteration

async def corout2():
    print("running corout2")
    await corout()


# make a coroutine
cr = corout()

#run it with a send:
cr.send(None)


cr2 = corout2()
cr2.send(None)


from types import coroutine

#Now we have a coroutine decorator with an await in it

@coroutine
def do_nothing():
    yield "something from do_nothing"


dn = do_nothing()
dn.send(None)

async def do_a_few_things(num=3):
    for i in range(num):
        print(f"in the loop for the {i}th time")
        res = await do_nothing()
        print("res is:", res)
    return "do a few things result"

daft = do_a_few_things(5)

#call up to 5 times
daft.send(None)

# to keep going, keep calling send() until we get the StopIteration

while True:
    try:
        daft.send(None)
    except StopIteration as si:
        print("The awaitable is complete")
        print("passed out:", si)
        break


# recell from generators that send naturally snd a val into the generator
def gen():
    for i in range(3):
        res = yield i
        print(f"loop: {i}, result: {res}")
    return "returned from gen"
g = gen()

# g.send(45)
# g.send(60)