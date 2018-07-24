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

--tela do fundo preto
local background = display.newRect(display.contentCenterX, display.contentCenterY, largura, altura)
	background:setFillColor(255,255,255)
--imagem do menu
local fundo_tela = display.newImageRect("Imagens_Jogo/topo.png", largura, 100)
	fundo_tela.anchorX = 0
	fundo_tela.anchorY = 0
--titulo "Menu"
local titulo = display.newText("Menu", 160, 40, "enchanted land", 50)
	titulo:setFillColor(0,0,0)
--Botões
local fundo_botao1 = display.newImageRect("Imagens_Jogo/Button_vazio.png", 210, 50)
	fundo_botao1.x = largura / 2
	fundo_botao1.y = 302

local botao1 = criar.newButton {
	label = "Criar Personagem",
	labelColor = {default={0,0,0}, over={0,255,0}},
	font = "enchanted land",
	fontSize = 32,
	x = largura / 2,
	y = 300
}

function botao1Tap()
	sc.gotoScene("criar_personagem", options)
end

botao1:addEventListener("tap", botao1Tap)

return scene