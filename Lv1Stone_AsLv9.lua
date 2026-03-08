-- Gem refinement: Lv1 stone/refinement treated as Lv9, failure = level down + stone consumed
-- 宝石精炼：1级石头和精炼石当9级用，失败掉级+石头消耗
-- Note: Each gem is refined independently by ITEMATTR_VAL_BaoshiLV; equipment gems do not conflict.

print("Loading Lv1Stone_AsLv9.lua")

local GEM_MAX_LEVEL = 9
local GEM_MIN_LEVEL = 1

-- Success rate per 1000: harder curve, 8->9 very tough
-- 1->2: 65%, 2->3: 50%, 3->4: 38%, 4->5: 28%, 5->6: 20%, 6->7: 14%, 7->8: 10%, 8->9: 7%
local SUCCESS_RATE = { [0]=700, [1]=650, [2]=500, [3]=380, [4]=280, [5]=200, [6]=140, [7]=100, [8]=70 }

local function doGemRefine(role, Item, actionName)
    local Item_Gem = GetChaItem(role, 2, 0)
    if Item_Gem == nil then
        SystemNotice(role, "背包第1格为空，请先将宝石放入第1格。")
        UseItemFailed(role)
        return
    end
    local gemLv = GetItemAttr(Item_Gem, ITEMATTR_VAL_BaoshiLV)
    if gemLv == nil then
        SystemNotice(role, "第1格物品不是宝石，无法"..actionName.."。")
        UseItemFailed(role)
        return
    end
    local gemId = GetItemID(Item_Gem)
    local gemName = GetItemName(gemId)
    local cha_name = GetChaDefaultName(role)

    if gemLv >= GEM_MAX_LEVEL then
        SystemNotice(role, "该宝石等级已达上限。")
        UseItemFailed(role)
        return
    end

    local successRate = SUCCESS_RATE[gemLv] or 250
    local roll = math.random(1, 1000)
    if roll <= successRate then
        SetItemAttr(Item_Gem, ITEMATTR_VAL_BaoshiLV, gemLv + 1)
        SynChaKitbag(role, 13)
        PlayEffect(role, 345)
        SystemNotice(role, "宝石"..actionName.."成功！["..gemName.."] "..(gemLv+1).."级")
        Notice("["..cha_name.."] 使用1级石头当9级，宝石"..actionName.."成功！["..gemName.."] "..(gemLv+1).."级")
    else
        local newLv = math.max(GEM_MIN_LEVEL, gemLv - 1)
        SetItemAttr(Item_Gem, ITEMATTR_VAL_BaoshiLV, newLv)
        TakeItem(role, 0, GetItemID(Item), 1)
        SynChaKitbag(role, 13)
        PlayEffect(role, 346)
        SystemNotice(role, "宝石"..actionName.."失败！["..gemName.."]掉级至"..newLv.."级，石头已消耗。")
        Notice("["..cha_name.."] 使用1级石头当9级，宝石"..actionName.."失败！["..gemName.."]掉级，石头爆了！")
    end
end

-- Lv1 enhancement stone on gem: 1级强化石当9级用
function ItemUse_Lv1Stone_AsLv9_Enhance(role, Item)
    doGemRefine(role, Item, "强化")
end

-- Lv1 refinement stone on gem: 1级精炼石当9级用
function ItemUse_Lv1Refine_AsLv9(role, Item)
    doGemRefine(role, Item, "精炼")
end
