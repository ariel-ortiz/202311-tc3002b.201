from wasmtime import Store, Module, Instance


def call_wasm_fun(file_name, fn_name, *args):
    with open(file_name) as file:
        wat_code = file.read()
    store = Store()
    module = Module(store.engine, wat_code)
    instance = Instance(store, module, [])
    entry_function = instance.exports(store)[fn_name]
    return entry_function(store, *args)


print(call_wasm_fun('simple.wat', 'meaning_of_life'))
print(call_wasm_fun('simple.wat', 'multiply', 11, 9))
print(call_wasm_fun('simple.wat', 'fahrenheit_to_celsuis', 212.0))
print(call_wasm_fun('simple.wat', 'fahrenheit_to_celsuis', 32.0))
print(call_wasm_fun('simple.wat', 'fahrenheit_to_celsuis', -40.0))
