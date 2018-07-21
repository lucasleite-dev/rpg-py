-- Importações
local sc = require("composer")
local  criar = require("widget")
--Variáveis
local scene = sc.newScene()
local largura = display.contentWidth
local altura = display.contentHeight

function scene:create( event )
 
    -- Assign "self.view" to local variable "sceneGroup" for easy reference
    local sceneGroup = self.view
 
    local menuBack = display.newRect( display.contentCenterX, display.contentCenterY, largura, altura)
    -- Insert object into "sceneGroup"
    sceneGroup:insert( menuBack )
end