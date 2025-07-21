using UnityEngine;
using System.Collections;

public class WaveManager : MonoBehaviour
{
    public EnemySpawner spawner;
    public Wave[] waves;

    private int currentWaveIndex = -1;
    private int enemiesSpawned = 0;

    void Start()
    {
        StartCoroutine(StartNextWave());
    }

    IEnumerator StartNextWave()
    {
        currentWaveIndex++;

        if (currentWaveIndex >= waves.Length)
        {
            Debug.Log("All waves completed!");
            yield break;
        }

        Wave currentWave = waves[currentWaveIndex];
        Debug.Log($"Starting Wave {currentWaveIndex + 1}");

        enemiesSpawned = 0;

        if (currentWave.waveType == WaveType.KillCount)
        {
            for (int i = 0; i < currentWave.enemyCount; i++)
            {
                spawner.SpawnEnemy();
                enemiesSpawned++;
                yield return new WaitForSeconds(currentWave.spawnInterval);
            }

            // Wait until all enemies are dead before starting next wave
            while (GameObject.FindGameObjectsWithTag("Enemy").Length > 0)
            {
                yield return null;
            }
        }
        else if (currentWave.waveType == WaveType.Timed)
        {
            float timer = 0f;

            while (timer < currentWave.duration)
            {
                spawner.SpawnEnemy();
                enemiesSpawned++;
                yield return new WaitForSeconds(currentWave.spawnInterval);
                timer += currentWave.spawnInterval;
            }

            // Wait until all enemies are killed before moving on
            while (GameObject.FindGameObjectsWithTag("Enemy").Length > 0)
            {
                yield return null;
            }
        }

        Debug.Log($"Wave {currentWaveIndex + 1} completed!");
        yield return StartCoroutine(StartNextWave());
    }
}
