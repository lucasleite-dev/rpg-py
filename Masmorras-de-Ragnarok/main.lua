-- Esconde barra de status do celular
display.setStatusBar( display.HiddenStatusBar )

-- Importações
local composer = require("composer")
local criar = require("widget")
--Variáveis
local scene = composer.newScene()
local largura = display.contentWidth
local altura = display.contentHeight

local options = {
    effect = "fade",
    time = 500,
    params = {
        someKey = "someValue",
        someOtherKey = 10
    }
}

local fundo_tela = display.newImageRect("Imagens_Jogo/tela_de_login.jpg", display.contentWidth, display.contentHeight)
fundo_tela.anchorX = 0
fundo_tela.anchorY = 0
fundo_tela.x = 0
fundo_tela.y = 0
--Botão
local botao = criar.newButton {
	defaultFile="Imagens_Jogo/botao_iniciarjogo.png",
	x = display.contentWidth/2, y = display.contentHeight/1.5,
	width = 120, height = 50,
	--onRelease = composer.gotoScene( "menu", options )
}
local titulo = display.newText("Dungeon of Ragnarok", 157, 90, "enchanted land", 38)

function botaoTap()
	composer.gotoScene( "menu", options )
	composer.removeScene( "main" )
end
botao:addEventListener( "tap" , botaoTap )