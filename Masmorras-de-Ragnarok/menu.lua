-- menu.lua
-- Importações
local sc = require("composer")
local cena = sc.newScene()
local  teste = require("widget")

function cena:criarCena( event )
	-- body
	local cenaGrupo = self.view

	local fundo_tela = display.newImageRect("Imagens_Jogo/tela_de_login.jpg", display.contentWidth, display.contentHeight)
	--fundo_tela.eixoX = 320
	fundo_tela.eixoY = 480
	fundo_tela.x, fundo_tela.y = 160, 180

	local titulo = display.newText("Dungeon of Ragnarok", 157, 90, "verdana", 28)
	--Botão
	local botao = teste.newButton {
		defaultFile="Imagens_Jogo/botao.png",
		x = display.contentWidth/2, y = display.contentHeight/1.5,
		width = 120, height = 120
		
	}
end

function  cena:entrarCena( event )
	
end

function  cena:sairCena( event )
	
end

cena:criarCena()

return cena