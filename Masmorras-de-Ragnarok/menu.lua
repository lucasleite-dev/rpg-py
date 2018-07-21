-- menu.lua
-- Importações
local sc = require("composer")
local  criar = require("widget")
--Variáveis
local scene = sc.newScene()
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

local botao 

function scene:create( event )
	local sceneGroup = self.view

	local fundo_tela = display.newImageRect("Imagens_Jogo/tela_de_login.jpg", display.contentWidth, display.contentHeight)
	fundo_tela.anchorX = 0
	fundo_tela.anchorY = 0
	fundo_tela.x = 0
	fundo_tela.y = 0

	local titulo = display.newText("Dungeon of Ragnarok", 157, 90, "verdana", 28)
	--Botão
	botao = criar.newButton {
		defaultFile="Imagens_Jogo/botao.png",
		x = display.contentWidth/2, y = display.contentHeight/1.5,
		width = 120, height = 120,
		onRelease = scene:destroy()
	}
	
	sceneGroup:insert(fundo_tela)
end

function scene:destroy( event )

	local sceneGroup = self.view

	if botao then
		cs.removeScene("menu")
		botao:removeSelf()
		botao = nil
		sc.gotoScene("personagens", options)
	end
end

scene:addEventListener( "create", scene )
scene:addEventListener( "destroy", scene )
return scene