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
 
    local telaCriacao = display.newRect( display.contentCenterX, display.contentCenterY, largura, altura)
    -- Insert object into "sceneGroup"
    local titulo2 = display.newText("Dungeon of Ragnarok", largura/2, altura/2, "verdana", 28)
    titulo2:setFillColor( 255,0,0 )
end

scene:addEventListener( "create", scene )

return scene