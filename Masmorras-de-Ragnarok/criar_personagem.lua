-- Importações
local sc = require("composer")
local  criar = require("widget")
--Variáveis
local scene = sc.newScene()
local largura = display.contentWidth
local altura = display.contentHeight
--tela do fundo preto
local background = display.newRect(display.contentCenterX, display.contentCenterY, largura, altura)
	background:setFillColor(255,255,255)
local titulo = display.newText("Menu", 160, 40, "enchanted land", 50)
	titulo:setFillColor(0,0,0)
local nome = io.read()

local nome_personagem = display.newText("Nome: " .. nome, 160, 40, "enchanted land", 50)
	titulo:setFillColor(0,0,0)
print(nome_personagem)

return scene