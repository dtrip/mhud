
function hud(x, y)
    local x,y,r = 0, 0, 1

        for i = 1, 360 do
            local angle = i * math.pi / 100;

            local ptx, pty = x + r * math.cos(angle), y + r * math.sin(angle);
            drawPoint(ptx, pty);
        end;
    return true;
end;

return hud
