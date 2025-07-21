using UnityEngine;

public class EnemySpawner : MonoBehaviour
{
    public GameObject[] enemyPrefabs;
    public Transform[] spawnPoints;

    public void SpawnEnemy()
    {
        if (spawnPoints.Length == 0 || enemyPrefabs.Length == 0)
            return;

        int randomIndex = Random.Range(0, spawnPoints.Length);
        int randomEnemy = Random.Range(0, enemyPrefabs.Length);

        Transform spawnPoint = spawnPoints[randomIndex];
        Instantiate(enemyPrefabs[randomEnemy], spawnPoint.position, spawnPoint.rotation);
    }
}
