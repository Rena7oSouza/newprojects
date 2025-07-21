using UnityEngine;

public class EnemyMovement : MonoBehaviour
{
    public EnemyInfo data;

    private Transform player;

    void Start()
    {
        player = GameObject.FindGameObjectWithTag("Player").transform;
    }

    void Update()
    {
        if (player != null && data != null)
        {
            LookToPlayer();
            MoveToPlayer();
        }
    }

    void MoveToPlayer()
    {
        Vector2 direction = (player.position - transform.position);
        float distance = direction.magnitude;

        if (distance > data.stoppingDistance)
        {
            Vector2 moveDir = direction.normalized;
            transform.position += (Vector3)(moveDir * data.moveSpeed * Time.deltaTime);
        }
    }

    void LookToPlayer()
    {
        Vector2 lookDir = player.position - transform.position;
        float angle = Mathf.Atan2(lookDir.y, lookDir.x) * Mathf.Rad2Deg;
        transform.rotation = Quaternion.Euler(0f, 0f, angle);
    }
}
