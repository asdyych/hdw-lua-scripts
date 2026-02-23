# -*- coding: utf-8 -*-
"""Append new ItemUse functions (10801q-10805q, 10806x-10813x, 3sxbox9, 4sxbox9) to ItemEffect.lua."""
import os

# New code block - English only to avoid encoding issues when writing as GBK
NEW_BLOCK = r'''
-- 1-5 level 1000-pack (qianlian) makeup boxes
function ItemUse_10801q(role, Item)
    local Item_CanGet = GetChaFreeBagGridNum(role)
    local cha_name = GetChaDefaultName(role)
    if Item_CanGet < 1 then
        SystemNotice(role, "Need at least 1 bag slot")
        UseItemFailed(role)
        return
    end
    local luck = math.random(1, 1000)
    if luck <= 200 then
        GiveItem(role, 0, 7021, 1000, 4)
        Notice("["..cha_name.."] opened 1-level makeup box (1000-pack), got 20k notes x1000!")
    elseif luck <= 650 then
        GiveItem(role, 0, 10832, 1, 4)
        Notice("["..cha_name.."] opened 1-level makeup box (1000-pack), got 2-level makeup box (1000-pack)!")
    elseif luck <= 660 then
        GiveItem(role, 0, 10833, 1, 4)
        Notice("["..cha_name.."] opened 1-level makeup box (1000-pack), got 3-level makeup box (1000-pack)!")
    elseif luck <= 662 then
        GiveItem(role, 0, 10834, 1, 4)
        Notice("["..cha_name.."] opened 1-level makeup box (1000-pack), got 4-level makeup box (1000-pack)!")
    elseif luck == 663 then
        GiveItem(role, 0, 10806, 1000, 4)
        Notice(">> Server: ["..cha_name.."] opened 1-level makeup box (1000-pack), blessed with 6-level makeup box x1000!")
    elseif luck <= 813 then
        GiveItem(role, 0, 5628, 1000, 4)
        Notice("["..cha_name.."] opened 1-level makeup box (1000-pack), got navigation lantern x1000!")
    elseif luck <= 963 then
        GiveItem(role, 0, 3105, 1000, 4)
        Notice("["..cha_name.."] opened 1-level makeup box (1000-pack), got walking lubricant x1000!")
    else
        GiveItem(role, 0, 2801, 1000, 4)
        Notice("["..cha_name.."] opened 1-level makeup box (1000-pack), got vent sandbag x1000!")
    end
end

function ItemUse_10802q(role, Item)
    local Item_CanGet = GetChaFreeBagGridNum(role)
    local cha_name = GetChaDefaultName(role)
    if Item_CanGet < 1 then
        SystemNotice(role, "Need at least 1 bag slot")
        UseItemFailed(role)
        return
    end
    local luck = math.random(1, 1000)
    if luck <= 200 then
        GiveItem(role, 0, 10831, 1, 4)
        Notice("["..cha_name.."] opened 2-level makeup box (1000-pack), got 1-level makeup box (1000-pack)!")
    elseif luck <= 650 then
        GiveItem(role, 0, 10833, 1, 4)
        Notice("["..cha_name.."] opened 2-level makeup box (1000-pack), got 3-level makeup box (1000-pack)!")
    elseif luck <= 660 then
        GiveItem(role, 0, 10834, 1, 4)
        Notice("["..cha_name.."] opened 2-level makeup box (1000-pack), got 4-level makeup box (1000-pack)!")
    elseif luck <= 662 then
        GiveItem(role, 0, 10835, 1, 4)
        Notice("["..cha_name.."] opened 2-level makeup box (1000-pack), got 5-level makeup box (1000-pack)!")
    elseif luck == 663 then
        GiveItem(role, 0, 10807, 1000, 4)
        Notice(">> Server: ["..cha_name.."] opened 2-level makeup box (1000-pack), blessed with 7-level makeup box x1000!")
    elseif luck <= 993 then
        GiveItem(role, 0, 885, 1000, 4)
        Notice("["..cha_name.."] opened 2-level makeup box (1000-pack), got refined stone x1000!")
    else
        GiveItem(role, 0, 2801, 1000, 4)
        Notice("["..cha_name.."] opened 2-level makeup box (1000-pack), got vent sandbag x1000!")
    end
end

function ItemUse_10803q(role, Item)
    local Item_CanGet = GetChaFreeBagGridNum(role)
    local cha_name = GetChaDefaultName(role)
    if Item_CanGet < 1 then
        SystemNotice(role, "Need at least 1 bag slot")
        UseItemFailed(role)
        return
    end
    local luck = math.random(1, 1000)
    if luck <= 200 then
        GiveItem(role, 0, 10832, 1, 4)
        Notice("["..cha_name.."] opened 3-level makeup box (1000-pack), got 2-level makeup box (1000-pack)!")
    elseif luck <= 650 then
        GiveItem(role, 0, 10834, 1, 4)
        Notice("["..cha_name.."] opened 3-level makeup box (1000-pack), got 4-level makeup box (1000-pack)!")
    elseif luck <= 660 then
        GiveItem(role, 0, 10805, 1000, 4)
        Notice("["..cha_name.."] opened 3-level makeup box (1000-pack), got 5-level makeup box x1000!")
    elseif luck <= 662 then
        GiveItem(role, 0, 10806, 1000, 4)
        Notice("["..cha_name.."] opened 3-level makeup box (1000-pack), got 6-level makeup box x1000!")
    elseif luck == 663 then
        GiveItem(role, 0, 10808, 1000, 4)
        Notice(">> Server: ["..cha_name.."] opened 3-level makeup box (1000-pack), blessed with 8-level makeup box x1000!")
    elseif luck <= 993 then
        GiveItem(role, 0, 10684, 1000, 4)
        Notice("["..cha_name.."] opened 3-level makeup box (1000-pack), got 3-attr gem box x1000!")
    else
        GiveItem(role, 0, 2801, 1000, 4)
        Notice("["..cha_name.."] opened 3-level makeup box (1000-pack), got vent sandbag x1000!")
    end
end

function ItemUse_10804q(role, Item)
    local Item_CanGet = GetChaFreeBagGridNum(role)
    local cha_name = GetChaDefaultName(role)
    if Item_CanGet < 1 then
        SystemNotice(role, "Need at least 1 bag slot")
        UseItemFailed(role)
        return
    end
    local luck = math.random(1, 1000)
    if luck <= 200 then
        GiveItem(role, 0, 10833, 1, 4)
        Notice("["..cha_name.."] opened 4-level makeup box (1000-pack), got 3-level makeup box (1000-pack)!")
    elseif luck <= 650 then
        GiveItem(role, 0, 10835, 1, 4)
        Notice("["..cha_name.."] opened 4-level makeup box (1000-pack), got 5-level makeup box (1000-pack)!")
    elseif luck <= 660 then
        GiveItem(role, 0, 10806, 1000, 4)
        Notice("["..cha_name.."] opened 4-level makeup box (1000-pack), got 6-level makeup box x1000!")
    elseif luck <= 662 then
        GiveItem(role, 0, 10807, 1000, 4)
        Notice("["..cha_name.."] opened 4-level makeup box (1000-pack), got 7-level makeup box x1000!")
    elseif luck == 663 then
        GiveItem(role, 0, 10809, 1000, 4)
        Notice(">> Server: ["..cha_name.."] opened 4-level makeup box (1000-pack), blessed with 9-level makeup box x1000!")
    elseif luck <= 763 then
        GiveItem(role, 0, 2326, 1000, 4)
        Notice("["..cha_name.."] opened 4-level makeup box (1000-pack), got real mask x1000!")
    elseif luck <= 993 then
        GiveItem(role, 0, 10685, 1000, 4)
        Notice("["..cha_name.."] opened 4-level makeup box (1000-pack), got 4-attr gem box x1000!")
    else
        GiveItem(role, 0, 853, 1000, 4)
        Notice("["..cha_name.."] opened 4-level makeup box (1000-pack), got magazine x1000!")
    end
end

function ItemUse_10805q(role, Item)
    local Item_CanGet = GetChaFreeBagGridNum(role)
    local cha_name = GetChaDefaultName(role)
    if Item_CanGet < 1 then
        SystemNotice(role, "Need at least 1 bag slot")
        UseItemFailed(role)
        return
    end
    local luck = math.random(1, 1000)
    if luck <= 200 then
        GiveItem(role, 0, 10834, 1, 4)
        Notice("["..cha_name.."] opened 5-level makeup box (1000-pack), got 4-level makeup box (1000-pack)!")
    elseif luck <= 650 then
        GiveItem(role, 0, 10806, 1000, 4)
        Notice("["..cha_name.."] opened 5-level makeup box (1000-pack), got 6-level makeup box x1000!")
    elseif luck <= 660 then
        GiveItem(role, 0, 10807, 1000, 4)
        Notice("["..cha_name.."] opened 5-level makeup box (1000-pack), got 7-level makeup box x1000!")
    elseif luck <= 662 then
        GiveItem(role, 0, 10808, 1000, 4)
        Notice("["..cha_name.."] opened 5-level makeup box (1000-pack), got 8-level makeup box x1000!")
    elseif luck == 663 then
        GiveItem(role, 0, 10810, 1000, 4)
        Notice(">> Server: ["..cha_name.."] opened 5-level makeup box (1000-pack), blessed with 10-level makeup box x1000!")
    elseif luck <= 993 then
        GiveItem(role, 0, 5629, 1000, 4)
        Notice("["..cha_name.."] opened 5-level makeup box (1000-pack), got super dumpling x1000!")
    else
        GiveItem(role, 0, 853, 1000, 4)
        Notice("["..cha_name.."] opened 5-level makeup box (1000-pack), got magazine x1000!")
    end
end

-- 6-13 level 10-pack makeup boxes (x10 open at once)
function ItemUse_10806x(role, Item)
    local Item_CanGet = GetChaFreeBagGridNum(role)
    local cha_name = GetChaDefaultName(role)
    if Item_CanGet < 1 then
        SystemNotice(role, "Need at least 1 bag slot")
        UseItemFailed(role)
        return
    end
    local luck = math.random(1, 1000)
    if luck <= 200 then
        GiveItem(role, 0, 10805, 10, 4)
    elseif luck <= 650 then
        GiveItem(role, 0, 10807, 10, 4)
    elseif luck <= 660 then
        GiveItem(role, 0, 10808, 10, 4)
        Notice("["..cha_name.."] 6-level makeup box (10-pack) got 8-level x10!")
    elseif luck <= 662 then
        GiveItem(role, 0, 10809, 10, 4)
        Notice("["..cha_name.."] 6-level makeup box (10-pack) got 9-level x10!")
    elseif luck == 663 then
        GiveItem(role, 0, 10811, 10, 4)
        Notice(">> ["..cha_name.."] 6-level makeup box (10-pack) blessed with 11-level x10!")
    elseif luck <= 763 then
        GiveItem(role, 0, 7071, 10, 4)
    elseif luck <= 863 then
        GiveItem(role, 0, 5629, 10, 4)
    elseif luck <= 993 then
        GiveItem(role, 0, 10623, 10, 4)
    else
        GiveItem(role, 0, 853, 10, 4)
        Notice("["..cha_name.."] 6-level makeup box (10-pack) got magazine x10!")
    end
end

function ItemUse_10807x(role, Item)
    local Item_CanGet = GetChaFreeBagGridNum(role)
    local cha_name = GetChaDefaultName(role)
    if Item_CanGet < 1 then
        SystemNotice(role, "Need at least 1 bag slot")
        UseItemFailed(role)
        return
    end
    local luck = math.random(1, 1000)
    if luck <= 200 then
        GiveItem(role, 0, 10806, 10, 4)
    elseif luck <= 650 then
        GiveItem(role, 0, 10808, 10, 4)
    elseif luck <= 660 then
        GiveItem(role, 0, 10809, 10, 4)
        Notice("["..cha_name.."] 7-level makeup box (10-pack) got 9-level x10!")
    elseif luck <= 662 then
        GiveItem(role, 0, 10810, 10, 4)
        Notice("["..cha_name.."] 7-level makeup box (10-pack) got 10-level x10!")
    elseif luck == 663 then
        GiveItem(role, 0, 10812, 10, 4)
        Notice(">> ["..cha_name.."] 7-level makeup box (10-pack) blessed with 12-level x10!")
    elseif luck <= 993 then
        GiveItem(role, 0, 6762, 10, 4)
    else
        GiveItem(role, 0, 853, 10, 4)
    end
end

function ItemUse_10808x(role, Item)
    local Item_CanGet = GetChaFreeBagGridNum(role)
    local cha_name = GetChaDefaultName(role)
    if Item_CanGet < 1 then
        SystemNotice(role, "Need at least 1 bag slot")
        UseItemFailed(role)
        return
    end
    local luck = math.random(1, 1000)
    if luck <= 200 then
        GiveItem(role, 0, 10807, 10, 4)
    elseif luck <= 650 then
        GiveItem(role, 0, 10809, 10, 4)
    elseif luck <= 660 then
        GiveItem(role, 0, 10810, 10, 4)
        Notice("["..cha_name.."] 8-level makeup box (10-pack) got 10-level x10!")
    elseif luck <= 662 then
        GiveItem(role, 0, 10811, 10, 4)
        Notice("["..cha_name.."] 8-level makeup box (10-pack) got 11-level x10!")
    elseif luck == 663 then
        GiveItem(role, 0, 10813, 10, 4)
        Notice(">> ["..cha_name.."] 8-level makeup box (10-pack) blessed with 13-level x10!")
    elseif luck <= 813 then
        GiveItem(role, 0, 3097, 10, 4)
    elseif luck <= 963 then
        GiveItem(role, 0, 10624, 10, 4)
        Notice("["..cha_name.."] 8-level makeup box (10-pack) got gem(4attr) x10!")
    else
        GiveItem(role, 0, 853, 10, 4)
    end
end

function ItemUse_10809x(role, Item)
    local Item_CanGet = GetChaFreeBagGridNum(role)
    local cha_name = GetChaDefaultName(role)
    if Item_CanGet < 1 then
        SystemNotice(role, "Need at least 1 bag slot")
        UseItemFailed(role)
        return
    end
    local luck = math.random(1, 1000)
    if luck <= 200 then
        GiveItem(role, 0, 10808, 10, 4)
        Notice("["..cha_name.."] 9-level makeup box (10-pack) got 8-level x10!")
    elseif luck <= 650 then
        GiveItem(role, 0, 10810, 10, 4)
        Notice("["..cha_name.."] 9-level makeup box (10-pack) got 10-level x10!")
    elseif luck <= 660 then
        GiveItem(role, 0, 10811, 10, 4)
        Notice("["..cha_name.."] 9-level makeup box (10-pack) got 11-level x10!")
    elseif luck <= 662 then
        GiveItem(role, 0, 10812, 10, 4)
        Notice("["..cha_name.."] 9-level makeup box (10-pack) got 12-level x10!")
    elseif luck == 663 then
        GiveItem(role, 0, 10814, 10, 4)
        Notice(">> ["..cha_name.."] 9-level makeup box (10-pack) blessed with 14-level x10!")
    elseif luck <= 763 then
        GiveItem(role, 0, 6762, 50, 4)
        Notice("["..cha_name.."] 9-level makeup box (10-pack) got gem powder x50!")
    elseif luck <= 913 then
        GiveItem(role, 0, 2728, 10, 4)
        Notice("["..cha_name.."] 9-level makeup box (10-pack) got happiness Lv2 x10!")
    elseif luck <= 963 then
        GiveItem(role, 0, 5629, 10, 4)
    else
        GiveItem(role, 0, 10683, 10, 4)
        Notice("["..cha_name.."] 9-level makeup box (10-pack) got gem fragment x10!")
    end
end

function ItemUse_10810x(role, Item)
    local Item_CanGet = GetChaFreeBagGridNum(role)
    local cha_name = GetChaDefaultName(role)
    if Item_CanGet < 1 then
        SystemNotice(role, "Need at least 1 bag slot")
        UseItemFailed(role)
        return
    end
    local luck = math.random(1, 1000)
    if luck <= 200 then
        GiveItem(role, 0, 10809, 10, 4)
        Notice("["..cha_name.."] 10-level makeup box (10-pack) got 9-level x10!")
    elseif luck <= 650 then
        GiveItem(role, 0, 10811, 10, 4)
        Notice("["..cha_name.."] 10-level makeup box (10-pack) got 11-level x10!")
    elseif luck <= 660 then
        GiveItem(role, 0, 10812, 10, 4)
        Notice("["..cha_name.."] 10-level makeup box (10-pack) got 12-level x10!")
    elseif luck <= 662 then
        GiveItem(role, 0, 10813, 10, 4)
        Notice("["..cha_name.."] 10-level makeup box (10-pack) got 13-level x10!")
    elseif luck == 663 then
        GiveItem(role, 0, 10815, 10, 4)
        Notice(">> ["..cha_name.."] 10-level makeup box (10-pack) blessed with 15-level x10!")
    elseif luck <= 763 then
        GiveItem(role, 0, 2752, 10, 4)
        Notice("["..cha_name.."] 10-level makeup box (10-pack) got happiness Lv3 x10!")
    elseif luck <= 863 then
        GiveItem(role, 0, 242, 10, 4)
        Notice("["..cha_name.."] 10-level makeup box (10-pack) got refined stone(4attr) x10!")
    elseif luck <= 963 then
        GiveItem(role, 0, 7345, 10, 4)
        Notice("["..cha_name.."] 10-level makeup box (10-pack) got gem fragment x10!")
    else
        GiveItem(role, 0, 2752, 10, 4)
        Notice("["..cha_name.."] 10-level makeup box (10-pack) got happiness Lv3 x10!")
    end
end

function ItemUse_10811x(role, Item)
    local Item_CanGet = GetChaFreeBagGridNum(role)
    local cha_name = GetChaDefaultName(role)
    if Item_CanGet < 1 then
        SystemNotice(role, "Need at least 1 bag slot")
        UseItemFailed(role)
        return
    end
    local luck = math.random(1, 1000)
    if luck <= 200 then
        GiveItem(role, 0, 10810, 10, 4)
        Notice("["..cha_name.."] 11-level makeup box (10-pack) got 10-level x10!")
    elseif luck <= 650 then
        GiveItem(role, 0, 10812, 10, 4)
        Notice("["..cha_name.."] 11-level makeup box (10-pack) got 12-level x10!")
    elseif luck <= 660 then
        GiveItem(role, 0, 10813, 10, 4)
        Notice("["..cha_name.."] 11-level makeup box (10-pack) got 13-level x10!")
    elseif luck <= 662 then
        GiveItem(role, 0, 10814, 10, 4)
        Notice("["..cha_name.."] 11-level makeup box (10-pack) got 14-level x10!")
    elseif luck == 663 then
        GiveItem(role, 0, 10816, 10, 4)
        Notice(">> ["..cha_name.."] 11-level makeup box (10-pack) blessed with 16-level x10!")
    elseif luck <= 813 then
        GiveItem(role, 0, 10689, 10, 4)
        Notice("["..cha_name.."] 11-level makeup box (10-pack) got gem fragment x10!")
    elseif luck <= 963 then
        GiveItem(role, 0, 7353, 10, 4)
        Notice("["..cha_name.."] 11-level makeup box (10-pack) got gem(4attr) x10!")
    else
        GiveItem(role, 0, 2752, 10, 4)
        Notice("["..cha_name.."] 11-level makeup box (10-pack) got happiness Lv3 x10!")
    end
end

function ItemUse_10812x(role, Item)
    local Item_CanGet = GetChaFreeBagGridNum(role)
    local cha_name = GetChaDefaultName(role)
    if Item_CanGet < 1 then
        SystemNotice(role, "Need at least 1 bag slot")
        UseItemFailed(role)
        return
    end
    local luck = math.random(1, 1000)
    if luck <= 250 then
        GiveItem(role, 0, 10811, 10, 4)
        Notice("["..cha_name.."] 12-level makeup box (10-pack) got 11-level x10!")
    elseif luck <= 650 then
        GiveItem(role, 0, 10813, 10, 4)
        Notice("["..cha_name.."] 12-level makeup box (10-pack) got 13-level x10!")
    elseif luck <= 660 then
        GiveItem(role, 0, 10814, 10, 4)
        Notice("["..cha_name.."] 12-level makeup box (10-pack) got 14-level x10!")
    elseif luck <= 662 then
        GiveItem(role, 0, 10815, 10, 4)
        Notice("["..cha_name.."] 12-level makeup box (10-pack) got 15-level x10!")
    elseif luck == 663 then
        GiveItem(role, 0, 10817, 10, 4)
        Notice(">> ["..cha_name.."] 12-level makeup box (10-pack) blessed with 17-level x10!")
    elseif luck <= 813 then
        GiveItem(role, 0, 10689, 10, 4)
        Notice("["..cha_name.."] 12-level makeup box (10-pack) got gem fragment x10!")
    elseif luck <= 963 then
        GiveItem(role, 0, 2515, 10, 4)
        Notice("["..cha_name.."] 12-level makeup box (10-pack) got gem(4attr) x10!")
    else
        GiveItem(role, 0, 2752, 10, 4)
        Notice("["..cha_name.."] 12-level makeup box (10-pack) got happiness Lv3 x10!")
    end
end

function ItemUse_10813x(role, Item)
    local Item_CanGet = GetChaFreeBagGridNum(role)
    local cha_name = GetChaDefaultName(role)
    if Item_CanGet < 1 then
        SystemNotice(role, "Need at least 1 bag slot")
        UseItemFailed(role)
        return
    end
    local luck = math.random(1, 1000)
    if luck <= 250 then
        GiveItem(role, 0, 10812, 10, 4)
        Notice("["..cha_name.."] 13-level makeup box (10-pack) got 12-level x10!")
    elseif luck <= 650 then
        GiveItem(role, 0, 10814, 10, 4)
        Notice("["..cha_name.."] 13-level makeup box (10-pack) got 14-level x10!")
    elseif luck <= 660 then
        GiveItem(role, 0, 10815, 10, 4)
        Notice("["..cha_name.."] 13-level makeup box (10-pack) got 15-level x10!")
    elseif luck <= 662 then
        GiveItem(role, 0, 10816, 10, 4)
        Notice("["..cha_name.."] 13-level makeup box (10-pack) got 16-level x10!")
    elseif luck == 663 then
        GiveItem(role, 0, 10818, 10, 4)
        Notice(">> ["..cha_name.."] 13-level makeup box (10-pack) blessed with 18-level x10!")
    elseif luck <= 713 then
        GiveItem(role, 0, 7500, 10, 4)
        Notice("["..cha_name.."] 13-level makeup box (10-pack) got gem(4attr) x10!")
    elseif luck <= 813 then
        GiveItem(role, 0, 2516, 10, 4)
        Notice("["..cha_name.."] 13-level makeup box (10-pack) got refined stone(4attr) x10!")
    elseif luck <= 963 then
        GiveItem(role, 0, 7291, 10, 4)
        Notice("["..cha_name.."] 13-level makeup box (10-pack) got gem fragment x10!")
    else
        GiveItem(role, 0, 2752, 10, 4)
        Notice("["..cha_name.."] 13-level makeup box (10-pack) got happiness Lv3 x10!")
    end
end

-- Level-9 3attr gem box (11250)
function ItemUse_3sxbox9(role, Item)
    local ItemID = GetItemID(Item)
    local ItemName = GetItemName(ItemID)
    local Cha_Boat = GetCtrlBoat(role)
    if Cha_Boat ~= nil then
        SystemNotice(role, "Cannot use "..ItemName.." on boat")
        UseItemFailed(role)
        return
    end
    local Item_CanGet = GetChaFreeBagGridNum(role)
    if Item_CanGet < 1 then
        SystemNotice(role, "Need at least 1 bag slot")
        UseItemFailed(role)
        return
    end
    local gemIds = {3490, 3491, 3492, 3493, 3494}
    local sc = math.random(1, #gemIds)
    local NewItemID = gemIds[sc]
    local item_name = GetItemName(NewItemID)
    GiveItem(role, 0, NewItemID, 1, 105)
    SystemNotice(role, "Opened level-9 3-attr gem box, got "..item_name.."")
end

-- Level-9 4attr gem box (11251)
function ItemUse_4sxbox9(role, Item)
    local ItemID = GetItemID(Item)
    local ItemName = GetItemName(ItemID)
    local Cha_Boat = GetCtrlBoat(role)
    if Cha_Boat ~= nil then
        SystemNotice(role, "Cannot use "..ItemName.." on boat")
        UseItemFailed(role)
        return
    end
    local Item_CanGet = GetChaFreeBagGridNum(role)
    if Item_CanGet < 1 then
        SystemNotice(role, "Need at least 1 bag slot")
        UseItemFailed(role)
        return
    end
    local gemIds = {3485, 3486, 3487, 3488, 3489}
    local sc = math.random(1, #gemIds)
    local NewItemID = gemIds[sc]
    local item_name = GetItemName(NewItemID)
    GiveItem(role, 0, NewItemID, 1, 105)
    SystemNotice(role, "Opened level-9 4-attr gem box, got "..item_name.."")
end

'''


def main():
    path = os.path.join(os.path.dirname(__file__), "ItemEffect.lua")
    with open(path, "r", encoding="gbk", newline="") as f:
        content = f.read()

    marker = "------------------潮声快乐器Lv1"
    if marker not in content:
        raise SystemExit("Marker not found")
    if "function ItemUse_10801q" in content:
        print("ItemUse_10801q already present, skip")
        return

    insert_pos = content.find(marker)
    new_content = content[:insert_pos] + NEW_BLOCK + "\n" + content[insert_pos:]

    with open(path, "w", encoding="gbk", newline="") as f:
        f.write(new_content)
    print("Patched ItemEffect.lua: added 10801q-10805q, 10806x-10813x, 3sxbox9, 4sxbox9")


if __name__ == "__main__":
    main()
