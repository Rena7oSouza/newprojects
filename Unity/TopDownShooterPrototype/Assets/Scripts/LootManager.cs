using UnityEngine;

public class LootManager : MonoBehaviour
{
    // Drop loot based on the EnemyInfo loot table
    public static void DropLoot(EnemyInfo data, Vector3 dropPosition)
    {
        foreach (LootData loot in data.lootTable)
        {
            int totalDropped = 0; // Track total quantity dropped for this item

            if (loot.maxQuantity <= 1)
            {
                // Single item drop chance
                float chance = loot.dropChance;
                if (Random.Range(0f, 100f) < chance)
                {
                    Instantiate(loot.itemPrefab, dropPosition, Quaternion.identity);
                    totalDropped = 1;
                }
            }
            else
            {
                // Multiple items with diminishing chance per extra unit
                int rolledQuantity = loot.minQuantity;

                for (int q = loot.minQuantity + 1; q <= loot.maxQuantity; q++)
                {
                    float chance = Mathf.Max(0f, 100f - (q - loot.minQuantity) * loot.decayRate);

                    if (Random.Range(0f, 100f) < chance)
                    {
                        rolledQuantity = q;
                    }
                    else
                    {
                        break; // stop increasing quantity if chance fails
                    }
                }

                for (int i = 0; i < rolledQuantity; i++)
                {
                    Instantiate(loot.itemPrefab, dropPosition, Quaternion.identity);
                }

                totalDropped = rolledQuantity;
            }

            // Debug.Log how many of this item were dropped
            Debug.Log($"Dropped {totalDropped} of {loot.itemPrefab.name}");
        }
    }
}
