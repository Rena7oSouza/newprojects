using UnityEngine;

public class Bullet : MonoBehaviour
{
    public float speed = 10f;
    public float lifeTime = 2f;
    public GameObject impactEffectPrefab;

    public float damage;

    void OnEnable()
    {
        Invoke("ReturnToPool", lifeTime);
    }

    void OnDisable()
    {
        CancelInvoke(); // Prevent errors if disabled before lifetime ends
    }

    void Update()
    {
        transform.Translate(Vector2.right * speed * Time.deltaTime);
    }

    void OnTriggerEnter2D(Collider2D other)
    {
        if (other.CompareTag("Enemy"))
        {
            EnemyHealth enemy = other.GetComponent<EnemyHealth>();
            if (enemy != null)
            {
                enemy.TakeDamage(damage);
            }
        }

        if (impactEffectPrefab != null)
            Instantiate(impactEffectPrefab, transform.position, Quaternion.identity);

        ReturnToPool();
    }

    void ReturnToPool()
    {
        BulletPool.Instance.ReturnBullet(gameObject);
    }
}
