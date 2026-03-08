-- Insert before line: ------------------潮声快乐器Lv1

-- 1-5级小叶子的化妆盒一千连
function ItemUse_10801q(role, Item)
    local Item_CanGet = GetChaFreeBagGridNum(role)
    local cha_name = GetChaDefaultName(role)
    if Item_CanGet < 1 then
        SystemNotice(role, "需要至少1个背包空格")
        UseItemFailed(role)
        return
    end
    local luck = math.random(1, 1000)
    if luck <= 200 then -- 20% 获得二万大钞x1000（与1级百连一致）
        GiveItem(role, 0, 7021, 1000, 4)
        Notice("玩家["..cha_name.."]开启1级小叶子的化妆盒一千连，获得二万大钞x1000！")
    elseif luck <= 650 then -- 45% 获得2级化妆盒一千连
        GiveItem(role, 0, 10832, 1, 4)
        Notice("玩家["..cha_name.."]开启1级小叶子的化妆盒一千连，获得2级化妆盒一千连！")
    elseif luck <= 660 then -- 1% 获得3级化妆盒一千连
        GiveItem(role, 0, 10833, 1, 4)
        Notice("玩家["..cha_name.."]开启1级小叶子的化妆盒一千连，获得3级化妆盒一千连！")
    elseif luck <= 662 then -- 0.2% 获得4级化妆盒一千连
        GiveItem(role, 0, 10834, 1, 4)
        Notice("玩家["..cha_name.."]开启1级小叶子的化妆盒一千连，获得4级化妆盒一千连！")
    elseif luck == 663 then -- 0.1% 神赐6级小叶子化妆盒x1000
        GiveItem(role, 0, 10806, 1000, 4)
        Notice(">> 全服通告：["..cha_name.."]开启1级小叶子的化妆盒一千连，神赐6级小叶子化妆盒x1000！")
    elseif luck <= 813 then -- 15% 获得领航灯笼x1000（与1级百连一致）
        GiveItem(role, 0, 5628, 1000, 4)
        Notice("玩家["..cha_name.."]开启1级小叶子的化妆盒一千连，获得领航灯笼x1000！")
    elseif luck <= 963 then -- 15% 获得行走润滑剂x1000（与1级百连一致）
        GiveItem(role, 0, 3105, 1000, 4)
        Notice("玩家["..cha_name.."]开启1级小叶子的化妆盒一千连，获得行走润滑剂x1000！")
    else -- 3.7% 获得发泄用沙包x1000（与1级百连一致）
        GiveItem(role, 0, 2801, 1000, 4)
        Notice("玩家["..cha_name.."]开启1级小叶子的化妆盒一千连，获得发泄用沙包x1000！")
    end
end

function ItemUse_10802q(role, Item)
    local Item_CanGet = GetChaFreeBagGridNum(role)
    local cha_name = GetChaDefaultName(role)
    if Item_CanGet < 1 then
        SystemNotice(role, "需要至少1个背包空格")
        UseItemFailed(role)
        return
    end
    local luck = math.random(1, 1000)
    if luck <= 200 then -- 20% 获得1级化妆盒一千连
        GiveItem(role, 0, 10831, 1, 4)
        Notice("玩家["..cha_name.."]开启2级小叶子的化妆盒一千连，获得1级化妆盒一千连！")
    elseif luck <= 650 then -- 45% 获得3级化妆盒一千连
        GiveItem(role, 0, 10833, 1, 4)
        Notice("玩家["..cha_name.."]开启2级小叶子的化妆盒一千连，获得3级化妆盒一千连！")
    elseif luck <= 660 then -- 1% 获得4级化妆盒一千连
        GiveItem(role, 0, 10834, 1, 4)
        Notice("玩家["..cha_name.."]开启2级小叶子的化妆盒一千连，获得4级化妆盒一千连！")
    elseif luck <= 662 then -- 0.2% 获得5级化妆盒一千连
        GiveItem(role, 0, 10835, 1, 4)
        Notice("玩家["..cha_name.."]开启2级小叶子的化妆盒一千连，获得5级化妆盒一千连！")
    elseif luck == 663 then -- 0.1% 神赐7级小叶子化妆盒x1000
        GiveItem(role, 0, 10807, 1000, 4)
        Notice(">> 全服通告：["..cha_name.."]开启2级小叶子的化妆盒一千连，神赐7级小叶子化妆盒x1000！")
    elseif luck <= 993 then -- 33% 获得精炼石x1000
        GiveItem(role, 0, 885, 1000, 4)
        Notice("玩家["..cha_name.."]开启2级小叶子的化妆盒一千连，获得精炼石x1000！")
    else -- 0.7% 获得发泄用沙包x1000（与2级百连一致）
        GiveItem(role, 0, 2801, 1000, 4)
        Notice("玩家["..cha_name.."]开启2级小叶子的化妆盒一千连，获得发泄用沙包x1000！")
    end
end

function ItemUse_10803q(role, Item)
    local Item_CanGet = GetChaFreeBagGridNum(role)
    local cha_name = GetChaDefaultName(role)
    if Item_CanGet < 1 then
        SystemNotice(role, "需要至少1个背包空格")
        UseItemFailed(role)
        return
    end
    local luck = math.random(1, 1000)
    if luck <= 200 then -- 20% 获得2级化妆盒一千连
        GiveItem(role, 0, 10832, 1, 4)
        Notice("玩家["..cha_name.."]开启3级小叶子的化妆盒一千连，获得2级化妆盒一千连！")
    elseif luck <= 650 then -- 45% 获得4级化妆盒一千连
        GiveItem(role, 0, 10834, 1, 4)
        Notice("玩家["..cha_name.."]开启3级小叶子的化妆盒一千连，获得4级化妆盒一千连！")
    elseif luck <= 660 then -- 1% 获得5级化妆盒x1000
        GiveItem(role, 0, 10805, 1000, 4)
        Notice("玩家["..cha_name.."]开启3级小叶子的化妆盒一千连，获得5级化妆盒x1000！")
    elseif luck <= 662 then -- 0.2% 获得6级化妆盒x1000
        GiveItem(role, 0, 10806, 1000, 4)
        Notice("玩家["..cha_name.."]开启3级小叶子的化妆盒一千连，获得6级化妆盒x1000！")
    elseif luck == 663 then -- 0.1% 神赐8级小叶子化妆盒x1000
        GiveItem(role, 0, 10808, 1000, 4)
        Notice(">> 全服通告：["..cha_name.."]开启3级小叶子的化妆盒一千连，神赐8级小叶子化妆盒x1000！")
    elseif luck <= 993 then -- 33% 获得3属性宝石箱x1000
        GiveItem(role, 0, 10684, 1000, 4)
        Notice("玩家["..cha_name.."]开启3级小叶子的化妆盒一千连，获得3属性宝石箱x1000！")
    else -- 0.7% 获得发泄用沙包x1000（与3级百连一致）
        GiveItem(role, 0, 2801, 1000, 4)
        Notice("玩家["..cha_name.."]开启3级小叶子的化妆盒一千连，获得发泄用沙包x1000！")
    end
end

function ItemUse_10804q(role, Item)
    local Item_CanGet = GetChaFreeBagGridNum(role)
    local cha_name = GetChaDefaultName(role)
    if Item_CanGet < 1 then
        SystemNotice(role, "需要至少1个背包空格")
        UseItemFailed(role)
        return
    end
    local luck = math.random(1, 1000)
    if luck <= 200 then -- 20% 获得3级化妆盒一千连
        GiveItem(role, 0, 10833, 1, 4)
        Notice("玩家["..cha_name.."]开启4级小叶子的化妆盒一千连，获得3级化妆盒一千连！")
    elseif luck <= 650 then -- 45% 获得5级化妆盒一千连
        GiveItem(role, 0, 10835, 1, 4)
        Notice("玩家["..cha_name.."]开启4级小叶子的化妆盒一千连，获得5级化妆盒一千连！")
    elseif luck <= 660 then -- 1% 获得6级化妆盒x1000
        GiveItem(role, 0, 10806, 1000, 4)
        Notice("玩家["..cha_name.."]开启4级小叶子的化妆盒一千连，获得6级化妆盒x1000！")
    elseif luck <= 662 then -- 0.2% 喜获7级小叶子化妆盒x1000
        GiveItem(role, 0, 10807, 1000, 4)
        Notice("玩家["..cha_name.."]开启4级小叶子的化妆盒一千连，喜获7级小叶子化妆盒x1000！")
    elseif luck == 663 then -- 0.1% 神赐9级小叶子化妆盒x1000
        GiveItem(role, 0, 10809, 1000, 4)
        Notice(">> 全服通告：["..cha_name.."]开启4级小叶子的化妆盒一千连，神赐9级小叶子化妆盒x1000！")
    elseif luck <= 763 then -- 10% 获得真实面具x1000
        GiveItem(role, 0, 2326, 1000, 4)
        Notice("玩家["..cha_name.."]开启4级小叶子的化妆盒一千连，获得真实面具x1000！")
    elseif luck <= 993 then -- 23% 获得4属性宝石箱x1000
        GiveItem(role, 0, 10685, 1000, 4)
        Notice("玩家["..cha_name.."]开启4级小叶子的化妆盒一千连，获得4属性宝石箱x1000！")
    else -- 0.7% 喜获假期欢乐杂志x1000（与4级百连一致）
        GiveItem(role, 0, 853, 1000, 4)
        Notice("玩家["..cha_name.."]开启4级小叶子的化妆盒一千连，喜获假期欢乐杂志x1000！")
    end
end

function ItemUse_10805q(role, Item)
    local Item_CanGet = GetChaFreeBagGridNum(role)
    local cha_name = GetChaDefaultName(role)
    if Item_CanGet < 1 then
        SystemNotice(role, "需要至少1个背包空格")
        UseItemFailed(role)
        return
    end
    local luck = math.random(1, 1000)
    if luck <= 200 then -- 20% 获得4级化妆盒一千连
        GiveItem(role, 0, 10834, 1, 4)
        Notice("玩家["..cha_name.."]开启5级小叶子的化妆盒一千连，获得4级化妆盒一千连！")
    elseif luck <= 650 then -- 45% 获得6级化妆盒x1000
        GiveItem(role, 0, 10806, 1000, 4)
        Notice("玩家["..cha_name.."]开启5级小叶子的化妆盒一千连，获得6级化妆盒x1000！")
    elseif luck <= 660 then -- 1% 喜获7级小叶子化妆盒x1000
        GiveItem(role, 0, 10807, 1000, 4)
        Notice("玩家["..cha_name.."]开启5级小叶子的化妆盒一千连，喜获7级小叶子化妆盒x1000！")
    elseif luck <= 662 then -- 0.2% 惊现8级小叶子化妆盒x1000
        GiveItem(role, 0, 10808, 1000, 4)
        Notice("玩家["..cha_name.."]开启5级小叶子的化妆盒一千连，惊现8级小叶子化妆盒x1000！")
    elseif luck == 663 then -- 0.1% 神赐10级小叶子化妆盒x1000
        GiveItem(role, 0, 10810, 1000, 4)
        Notice(">> 全服通告：["..cha_name.."]开启5级小叶子的化妆盒一千连，神赐10级小叶子化妆盒x1000！")
    elseif luck <= 993 then -- 33% 获得超人水饺x1000
        GiveItem(role, 0, 5629, 1000, 4)
        Notice("玩家["..cha_name.."]开启5级小叶子的化妆盒一千连，获得超人水饺x1000！")
    else -- 0.7% 获得假期欢乐杂志x1000
        GiveItem(role, 0, 853, 1000, 4)
        Notice("玩家["..cha_name.."]开启5级小叶子的化妆盒一千连，获得假期欢乐杂志x1000！")
    end
end

-- 6-13级小叶子的化妆盒十连
function ItemUse_10806x(role, Item)
    local Item_CanGet = GetChaFreeBagGridNum(role)
    local cha_name = GetChaDefaultName(role)
    if Item_CanGet < 1 then
        SystemNotice(role, "需要至少1个背包空格")
        UseItemFailed(role)
        return
    end
    local luck = math.random(1, 1000)
    if luck <= 200 then -- 20% 获得5级化妆盒x10
        GiveItem(role, 0, 10805, 10, 4)
    elseif luck <= 650 then -- 45% 获得7级化妆盒x10
        GiveItem(role, 0, 10807, 10, 4)
    elseif luck <= 660 then -- 1% 获得8级化妆盒x10
        GiveItem(role, 0, 10808, 10, 4)
        Notice("玩家["..cha_name.."]开启6级小叶子的化妆盒十连，获得8级化妆盒x10！")
    elseif luck <= 662 then -- 0.2% 获得9级化妆盒x10
        GiveItem(role, 0, 10809, 10, 4)
        Notice("玩家["..cha_name.."]开启6级小叶子的化妆盒十连，获得9级化妆盒x10！")
    elseif luck == 663 then -- 0.1% 神赐11级小叶子化妆盒x10
        GiveItem(role, 0, 10811, 10, 4)
        Notice(">> 全服通告：["..cha_name.."]开启6级小叶子的化妆盒十连，神赐11级小叶子化妆盒x10！")
    elseif luck <= 763 then -- 10% 获得翅膀宝箱x10（与6级单开一致）
        GiveItem(role, 0, 7071, 10, 4)
    elseif luck <= 863 then -- 10% 获得超人饺子x10（与6级单开一致）
        GiveItem(role, 0, 5629, 10, 4)
    elseif luck <= 993 then -- 13% 获得楪子零食包x10（与6级单开一致）
        GiveItem(role, 0, 10623, 10, 4)
    else -- 0.7% 获得假期欢乐杂志x10（与6级单开一致）
        GiveItem(role, 0, 853, 10, 4)
        Notice("玩家["..cha_name.."]开启6级小叶子的化妆盒十连，获得假期欢乐杂志x10！")
    end
end

function ItemUse_10807x(role, Item)
    local Item_CanGet = GetChaFreeBagGridNum(role)
    local cha_name = GetChaDefaultName(role)
    if Item_CanGet < 1 then
        SystemNotice(role, "需要至少1个背包空格")
        UseItemFailed(role)
        return
    end
    local luck = math.random(1, 1000)
    if luck <= 200 then -- 20% 获得6级化妆盒x10
        GiveItem(role, 0, 10806, 10, 4)
    elseif luck <= 650 then -- 45% 获得8级化妆盒x10
        GiveItem(role, 0, 10808, 10, 4)
    elseif luck <= 660 then -- 1% 获得9级化妆盒x10
        GiveItem(role, 0, 10809, 10, 4)
        Notice("玩家["..cha_name.."]开启7级小叶子的化妆盒十连，获得9级化妆盒x10！")
    elseif luck <= 662 then -- 0.2% 获得10级化妆盒x10
        GiveItem(role, 0, 10810, 10, 4)
        Notice("玩家["..cha_name.."]开启7级小叶子的化妆盒十连，获得10级化妆盒x10！")
    elseif luck == 663 then -- 0.1% 神赐12级小叶子化妆盒x10
        GiveItem(role, 0, 10812, 10, 4)
        Notice(">> 全服通告：["..cha_name.."]开启7级小叶子的化妆盒十连，神赐12级小叶子化妆盒x10！")
    elseif luck <= 993 then -- 33% 获得高级强化晶石x10（与7级单开一致）
        GiveItem(role, 0, 6762, 10, 4)
    else -- 0.7% 获得假期欢乐杂志x10（与7级单开一致）
        GiveItem(role, 0, 853, 10, 4)
    end
end

function ItemUse_10808x(role, Item)
    local Item_CanGet = GetChaFreeBagGridNum(role)
    local cha_name = GetChaDefaultName(role)
    if Item_CanGet < 1 then
        SystemNotice(role, "需要至少1个背包空格")
        UseItemFailed(role)
        return
    end
    local luck = math.random(1, 1000)
    if luck <= 200 then -- 20% 获得7级化妆盒x10
        GiveItem(role, 0, 10807, 10, 4)
    elseif luck <= 650 then -- 45% 获得9级化妆盒x10
        GiveItem(role, 0, 10809, 10, 4)
    elseif luck <= 660 then -- 1% 获得10级化妆盒x10
        GiveItem(role, 0, 10810, 10, 4)
        Notice("玩家["..cha_name.."]开启8级小叶子的化妆盒十连，获得10级化妆盒x10！")
    elseif luck <= 662 then -- 0.2% 获得11级化妆盒x10
        GiveItem(role, 0, 10811, 10, 4)
        Notice("玩家["..cha_name.."]开启8级小叶子的化妆盒十连，获得11级化妆盒x10！")
    elseif luck == 663 then -- 0.1% 神赐13级小叶子化妆盒x10
        GiveItem(role, 0, 10813, 10, 4)
        Notice(">> 全服通告：["..cha_name.."]开启8级小叶子的化妆盒十连，神赐13级小叶子化妆盒x10！")
    elseif luck <= 813 then -- 15% 获得高级财富增幅器x10（与8级单开一致）
        GiveItem(role, 0, 3097, 10, 4)
    elseif luck <= 963 then -- 15% 获得楪子信封x10（与8级单开一致）
        GiveItem(role, 0, 10624, 10, 4)
        Notice("玩家["..cha_name.."]开启8级小叶子的化妆盒十连，获得楪子信封(戒指)x10！")
    else -- 3.7% 获得假期欢乐杂志x10（与8级单开一致）
        GiveItem(role, 0, 853, 10, 4)
    end
end

function ItemUse_10809x(role, Item)
    local Item_CanGet = GetChaFreeBagGridNum(role)
    local cha_name = GetChaDefaultName(role)
    if Item_CanGet < 1 then
        SystemNotice(role, "需要至少1个背包空格")
        UseItemFailed(role)
        return
    end
    local luck = math.random(1, 1000)
    if luck <= 200 then -- 20% 获得8级化妆盒x10
        GiveItem(role, 0, 10808, 10, 4)
        Notice("玩家["..cha_name.."]开启9级小叶子的化妆盒十连，获得8级化妆盒x10！")
    elseif luck <= 650 then -- 45% 获得10级化妆盒x10
        GiveItem(role, 0, 10810, 10, 4)
        Notice("玩家["..cha_name.."]开启9级小叶子的化妆盒十连，获得10级化妆盒x10！")
    elseif luck <= 660 then -- 1% 获得11级化妆盒x10
        GiveItem(role, 0, 10811, 10, 4)
        Notice("玩家["..cha_name.."]开启9级小叶子的化妆盒十连，获得11级化妆盒x10！")
    elseif luck <= 662 then -- 0.2% 获得12级化妆盒x10
        GiveItem(role, 0, 10812, 10, 4)
        Notice("玩家["..cha_name.."]开启9级小叶子的化妆盒十连，获得12级化妆盒x10！")
    elseif luck == 663 then -- 0.1% 神赐14级小叶子化妆盒x10
        GiveItem(role, 0, 10814, 10, 4)
        Notice(">> 全服通告：["..cha_name.."]开启9级小叶子的化妆盒十连，神赐14级小叶子化妆盒x10！")
    elseif luck <= 763 then -- 10% 获得高级强化晶石x50（与9级单开一致）
        GiveItem(role, 0, 6762, 50, 4)
        Notice("玩家["..cha_name.."]开启9级小叶子的化妆盒十连，获得高级强化晶石x50！")
    elseif luck <= 913 then -- 15% 获得邪恶发生器Lv2 x10（与9级单开一致）
        GiveItem(role, 0, 2728, 10, 4)
        Notice("玩家["..cha_name.."]开启9级小叶子的化妆盒十连，获得邪恶发生器Lv2 x10！")
    elseif luck <= 963 then -- 5% 获得超人水饺x10（与9级单开一致）
        GiveItem(role, 0, 5629, 10, 4)
    else -- 3.7% 获得披风宝石箱x10（与9级单开一致）
        GiveItem(role, 0, 10683, 10, 4)
        Notice("玩家["..cha_name.."]开启9级小叶子的化妆盒十连，获得披风宝石箱x10！")
    end
end

function ItemUse_10810x(role, Item)
    local Item_CanGet = GetChaFreeBagGridNum(role)
    local cha_name = GetChaDefaultName(role)
    if Item_CanGet < 1 then
        SystemNotice(role, "需要至少1个背包空格")
        UseItemFailed(role)
        return
    end
    local luck = math.random(1, 1000)
    if luck <= 200 then -- 20% 获得9级化妆盒x10
        GiveItem(role, 0, 10809, 10, 4)
        Notice("玩家["..cha_name.."]开启10级小叶子的化妆盒十连，获得9级化妆盒x10！")
    elseif luck <= 650 then -- 45% 获得11级化妆盒x10
        GiveItem(role, 0, 10811, 10, 4)
        Notice("玩家["..cha_name.."]开启10级小叶子的化妆盒十连，获得11级化妆盒x10！")
    elseif luck <= 660 then -- 1% 获得12级化妆盒x10
        GiveItem(role, 0, 10812, 10, 4)
        Notice("玩家["..cha_name.."]开启10级小叶子的化妆盒十连，获得12级化妆盒x10！")
    elseif luck <= 662 then -- 0.2% 获得13级化妆盒x10
        GiveItem(role, 0, 10813, 10, 4)
        Notice("玩家["..cha_name.."]开启10级小叶子的化妆盒十连，获得13级化妆盒x10！")
    elseif luck == 663 then -- 0.1% 神赐15级小叶子化妆盒x10
        GiveItem(role, 0, 10815, 10, 4)
        Notice(">> 全服通告：["..cha_name.."]开启10级小叶子的化妆盒十连，神赐15级小叶子化妆盒x10！")
    elseif luck <= 763 then -- 10% 获得邪恶发生器Lv3 x10（与10级单开一致）
        GiveItem(role, 0, 2752, 10, 4)
        Notice("玩家["..cha_name.."]开启10级小叶子的化妆盒十连，获得邪恶发生器Lv3 x10！")
    elseif luck <= 863 then -- 10% 获得好看楪子嫁妆盒x10（与10级单开一致）
        GiveItem(role, 0, 242, 10, 4)
        Notice("玩家["..cha_name.."]开启10级小叶子的化妆盒十连，获得好看楪子嫁妆盒(戒指)x10！")
    elseif luck <= 963 then -- 10% 获得披风加工器x10（与10级单开一致）
        GiveItem(role, 0, 7345, 10, 4)
        Notice("玩家["..cha_name.."]开启10级小叶子的化妆盒十连，获得披风加工器x10！")
    else -- 3.7% 获得邪恶发生器Lv3 x10（与10级单开一致）
        GiveItem(role, 0, 2752, 10, 4)
        Notice("玩家["..cha_name.."]开启10级小叶子的化妆盒十连，获得邪恶发生器Lv3 x10！")
    end
end

function ItemUse_10811x(role, Item)
    local Item_CanGet = GetChaFreeBagGridNum(role)
    local cha_name = GetChaDefaultName(role)
    if Item_CanGet < 1 then
        SystemNotice(role, "需要至少1个背包空格")
        UseItemFailed(role)
        return
    end
    local luck = math.random(1, 1000)
    if luck <= 200 then -- 20% 获得10级化妆盒x10
        GiveItem(role, 0, 10810, 10, 4)
        Notice("玩家["..cha_name.."]开启11级小叶子的化妆盒十连，获得10级化妆盒x10！")
    elseif luck <= 650 then -- 45% 获得12级化妆盒x10
        GiveItem(role, 0, 10812, 10, 4)
        Notice("玩家["..cha_name.."]开启11级小叶子的化妆盒十连，获得12级化妆盒x10！")
    elseif luck <= 660 then -- 1% 获得13级化妆盒x10
        GiveItem(role, 0, 10813, 10, 4)
        Notice("玩家["..cha_name.."]开启11级小叶子的化妆盒十连，获得13级化妆盒x10！")
    elseif luck <= 662 then -- 0.2% 获得14级化妆盒x10
        GiveItem(role, 0, 10814, 10, 4)
        Notice("玩家["..cha_name.."]开启11级小叶子的化妆盒十连，获得14级化妆盒x10！")
    elseif luck == 663 then -- 0.1% 神赐16级小叶子化妆盒x10
        GiveItem(role, 0, 10816, 10, 4)
        Notice(">> 全服通告：["..cha_name.."]开启11级小叶子的化妆盒十连，神赐16级小叶子化妆盒x10！")
    elseif luck <= 813 then -- 15% 获得死神宝石箱x10（与11级单开一致）
        GiveItem(role, 0, 10689, 10, 4)
        Notice("玩家["..cha_name.."]开启11级小叶子的化妆盒十连，获得死神宝石箱x10！")
    elseif luck <= 963 then -- 15% 获得背后精灵宝箱(一代)x10（与11级单开一致）
        GiveItem(role, 0, 7353, 10, 4)
        Notice("玩家["..cha_name.."]开启11级小叶子的化妆盒十连，获得背后精灵宝箱(一代)x10！")
    else -- 3.7% 获得邪恶发生器Lv3 x10（与11级单开一致）
        GiveItem(role, 0, 2752, 10, 4)
        Notice("玩家["..cha_name.."]开启11级小叶子的化妆盒十连，获得邪恶发生器Lv3 x10！")
    end
end

function ItemUse_10812x(role, Item)
    local Item_CanGet = GetChaFreeBagGridNum(role)
    local cha_name = GetChaDefaultName(role)
    if Item_CanGet < 1 then
        SystemNotice(role, "需要至少1个背包空格")
        UseItemFailed(role)
        return
    end
    local luck = math.random(1, 1000)
    if luck <= 250 then -- 25% 获得11级化妆盒x10（与12级单开一致）
        GiveItem(role, 0, 10811, 10, 4)
        Notice("玩家["..cha_name.."]开启12级小叶子的化妆盒十连，获得11级化妆盒x10！")
    elseif luck <= 650 then -- 40% 获得13级化妆盒x10（与12级单开一致）
        GiveItem(role, 0, 10813, 10, 4)
        Notice("玩家["..cha_name.."]开启12级小叶子的化妆盒十连，获得13级化妆盒x10！")
    elseif luck <= 660 then -- 1% 获得14级化妆盒x10
        GiveItem(role, 0, 10814, 10, 4)
        Notice("玩家["..cha_name.."]开启12级小叶子的化妆盒十连，获得14级化妆盒x10！")
    elseif luck <= 662 then -- 0.2% 获得15级化妆盒x10
        GiveItem(role, 0, 10815, 10, 4)
        Notice("玩家["..cha_name.."]开启12级小叶子的化妆盒十连，获得15级化妆盒x10！")
    elseif luck == 663 then -- 0.1% 神赐17级小叶子化妆盒x10
        GiveItem(role, 0, 10817, 10, 4)
        Notice(">> 全服通告：["..cha_name.."]开启12级小叶子的化妆盒十连，神赐17级小叶子化妆盒x10！")
    elseif luck <= 813 then -- 15% 获得死神宝石箱x10（与12级单开一致）
        GiveItem(role, 0, 10689, 10, 4)
        Notice("玩家["..cha_name.."]开启12级小叶子的化妆盒十连，获得死神宝石箱x10！")
    elseif luck <= 963 then -- 15% 获得精致嫁妆盒(戒指)x10（与12级单开一致）
        GiveItem(role, 0, 2515, 10, 4)
        Notice("玩家["..cha_name.."]开启12级小叶子的化妆盒十连，获得精致嫁妆盒(戒指)x10！")
    else -- 3.7% 获得邪恶发生器Lv3 x10（与12级单开一致）
        GiveItem(role, 0, 2752, 10, 4)
        Notice("玩家["..cha_name.."]开启12级小叶子的化妆盒十连，获得邪恶发生器Lv3 x10！")
    end
end

function ItemUse_10813x(role, Item)
    local Item_CanGet = GetChaFreeBagGridNum(role)
    local cha_name = GetChaDefaultName(role)
    if Item_CanGet < 1 then
        SystemNotice(role, "需要至少1个背包空格")
        UseItemFailed(role)
        return
    end
    local luck = math.random(1, 1000)
    if luck <= 250 then -- 25% 获得12级化妆盒x10（与13级单开一致）
        GiveItem(role, 0, 10812, 10, 4)
        Notice("玩家["..cha_name.."]开启13级小叶子的化妆盒十连，获得12级化妆盒x10！")
    elseif luck <= 650 then -- 40% 获得14级化妆盒x10（与13级单开一致）
        GiveItem(role, 0, 10814, 10, 4)
        Notice("玩家["..cha_name.."]开启13级小叶子的化妆盒十连，获得14级化妆盒x10！")
    elseif luck <= 660 then -- 1% 获得15级化妆盒x10
        GiveItem(role, 0, 10815, 10, 4)
        Notice("玩家["..cha_name.."]开启13级小叶子的化妆盒十连，获得15级化妆盒x10！")
    elseif luck <= 662 then -- 0.2% 获得16级化妆盒x10
        GiveItem(role, 0, 10816, 10, 4)
        Notice("玩家["..cha_name.."]开启13级小叶子的化妆盒十连，获得16级化妆盒x10！")
    elseif luck == 663 then -- 0.1% 神赐18级小叶子化妆盒x10
        GiveItem(role, 0, 10818, 10, 4)
        Notice(">> 全服通告：["..cha_name.."]开启13级小叶子的化妆盒十连，神赐18级小叶子化妆盒x10！")
    elseif luck <= 713 then -- 5% 获得坐骑宝箱(初级)x10（与13级单开一致）
        GiveItem(role, 0, 7500, 10, 4)
        Notice("玩家["..cha_name.."]开启13级小叶子的化妆盒十连，获得坐骑宝箱(初级)x10！")
    elseif luck <= 813 then -- 10% 获得璀璨楪子嫁妆盒(戒指)x10（与13级单开一致）
        GiveItem(role, 0, 2516, 10, 4)
        Notice("玩家["..cha_name.."]开启13级小叶子的化妆盒十连，获得璀璨楪子嫁妆盒(戒指)x10！")
    elseif luck <= 963 then -- 15% 获得恶魔首饰宝箱x10（与13级单开一致）
        GiveItem(role, 0, 7291, 10, 4)
        Notice("玩家["..cha_name.."]开启13级小叶子的化妆盒十连，获得恶魔首饰宝箱x10！")
    else -- 3.7% 获得邪恶发生器Lv3 x10（与13级单开一致）
        GiveItem(role, 0, 2752, 10, 4)
        Notice("玩家["..cha_name.."]开启13级小叶子的化妆盒十连，获得邪恶发生器Lv3 x10！")
    end
end

-- Level-9 3attr gem box (11250)
function ItemUse_3sxbox9(role, Item)
    local ItemID = GetItemID(Item)
    local ItemName = GetItemName(ItemID)
    local Cha_Boat = GetCtrlBoat(role)
    if Cha_Boat ~= nil then
        SystemNotice(role, "船上不可使用"..ItemName)
        UseItemFailed(role)
        return
    end
    local Item_CanGet = GetChaFreeBagGridNum(role)
    if Item_CanGet < 1 then
        SystemNotice(role, "需要至少1个背包空格")
        UseItemFailed(role)
        return
    end
    local gemIds = {3490, 3491, 3492, 3493, 3494}
    local sc = math.random(1, #gemIds)
    local NewItemID = gemIds[sc]
    local item_name = GetItemName(NewItemID)
    GiveItem(role, 0, NewItemID, 1, 105)
    SystemNotice(role, "开启九级3属性宝石宝箱，获得"..item_name.."")
end

-- Level-9 4attr gem box (11251)
function ItemUse_4sxbox9(role, Item)
    local ItemID = GetItemID(Item)
    local ItemName = GetItemName(ItemID)
    local Cha_Boat = GetCtrlBoat(role)
    if Cha_Boat ~= nil then
        SystemNotice(role, "船上不可使用"..ItemName)
        UseItemFailed(role)
        return
    end
    local Item_CanGet = GetChaFreeBagGridNum(role)
    if Item_CanGet < 1 then
        SystemNotice(role, "需要至少1个背包空格")
        UseItemFailed(role)
        return
    end
    local gemIds = {3485, 3486, 3487, 3488, 3489}
    local sc = math.random(1, #gemIds)
    local NewItemID = gemIds[sc]
    local item_name = GetItemName(NewItemID)
    GiveItem(role, 0, NewItemID, 1, 105)
    SystemNotice(role, "开启九级4属性宝石宝箱，获得"..item_name.."")
end

################################################################################
