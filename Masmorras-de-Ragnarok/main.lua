-- Esconde barra de status do celular
display.setStatusBar( display.HiddenStatusBar )

local sc = require("composer")

local options = {
    effect = "fade",
    time = 500,
    params = {
        someKey = "someValue",
        someOtherKey = 10
    }
}

sc.gotoScene("menu", options)
