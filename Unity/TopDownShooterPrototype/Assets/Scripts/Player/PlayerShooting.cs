using UnityEngine;
using UnityEngine.InputSystem;

public class PlayerShooting : MonoBehaviour
{
    public GameObject bulletPrefab;
    public Transform firePoint;
    public float baseDamage = 1f;
    public float fireRate = 0.5f;
    public float reloadSpeed = 1.0f;
    public int magazineSize = 10;
    public GameObject muzzleFlashPrefab;

    private float nextFireTime = 0f;
    private int currentAmmo;
    private SkillTreeManager skillTreeManager;
    private PlayerControls controls;
    private SimulateMobile simulateMobile;

    void Awake()
    {
        controls = new PlayerControls();
        simulateMobile = GetComponent<SimulateMobile>();
        skillTreeManager = GetComponent<SkillTreeManager>();

        currentAmmo = magazineSize;

        controls.Player.Shoot.performed += ctx => PerformShoot();
    }

    void OnEnable() => controls.Enable();
    void OnDisable() => controls.Disable();

    void PerformShoot()
    {
        if (Time.time < nextFireTime || currentAmmo <= 0)
            return;

        float damage = CalculateDamage();

        GameObject bullet = BulletPool.Instance.GetBullet();
        bullet.transform.position = firePoint.position;
        bullet.transform.rotation = firePoint.rotation;
        bullet.GetComponent<Bullet>().damage = damage;


        nextFireTime = Time.time + fireRate;
        currentAmmo--;

        AudioManager.Instance.Play("Shoot");
        Instantiate(muzzleFlashPrefab, firePoint.position, firePoint.rotation);
    }

    float CalculateDamage()
    {
        float finalDamage = baseDamage;
        Debug.Log(baseDamage);
        // Get skill bonus for pistol as example
        Skill pistolSkill = skillTreeManager.GetSkill("Pistol Mastery Lv1");
        if (pistolSkill != null && pistolSkill.bonusType == SkillBonusType.Damage)
        {
            finalDamage += baseDamage * pistolSkill.bonusValue;
            Debug.Log(pistolSkill.bonusValue);
        }

        return finalDamage;
    }

    public void Reload()
    {
        // Apply reload speed from skills if any
        Skill reloadSkill = skillTreeManager.GetSkill("Pistol Mastery Lv2");
        float reloadTime = reloadSpeed;
        if (reloadSkill != null && reloadSkill.bonusType == SkillBonusType.ReloadSpeed)
        {
            reloadTime -= reloadSkill.bonusValue;
        }

        // Example reload logic with coroutine:
        StartCoroutine(ReloadCoroutine(reloadTime));
    }

    System.Collections.IEnumerator ReloadCoroutine(float reloadTime)
    {
        yield return new WaitForSeconds(reloadTime);
        currentAmmo = magazineSize;

        // If there is a magazine size bonus skill:
        Skill magSkill = skillTreeManager.GetSkill("Pistol Mastery Lv3");
        if (magSkill != null && magSkill.bonusType == SkillBonusType.MagazineSize)
        {
            currentAmmo += (int)magSkill.bonusValue;
        }
    }
}
