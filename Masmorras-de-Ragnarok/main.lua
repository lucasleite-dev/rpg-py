-- Esconde barra de status do celular
display.setStatusBar( display.HiddenStatusBar )

-- Importações
local composer = require("composer")
local criar = require("widget")
--Variáveis
local scene = composer.newScene()
local largura = display.contentWidth
local altura = display.contentHeight

local _CX = display.contentCenterX
local _CY = display.contentCenterY
local imgW = 440 -- width of image 
local imgH = 623 -- height of image
local imgR = imgH / imgW
local screenW = display.contentWidth - 2 * display.screenOriginX 
local screenH = display.contentHeight - 2 * display.screenOriginY 
local screenR = screenH / screenW
local factor = imgR > screenR and screenW / imgW or screenH / imgH


local options = {
    effect = "fade",
    time = 500,
    params = {
        someKey = "someValue",
        someOtherKey = 10
    }
}

local fundo_tela = display.newImageRect("Imagens_Jogo/tela_de_login.jpg",  imgW * factor, imgH * factor )
fundo_tela.x = largura/2
fundo_tela.y = altura/2
--Botão
local botao = criar.newButton {
	defaultFile="Imagens_Jogo/botao_iniciarjogo.png",
	x = display.contentWidth/2, y = display.contentHeight/1.5,
	width = 120, height = 50,
	--onRelease = composer.gotoScene( "menu", options )
}

function botaoTap()
	composer.gotoScene( "menu", options )
	composer.removeScene( "main" )
end
botao:addEventListener( "tap" , botaoTap )