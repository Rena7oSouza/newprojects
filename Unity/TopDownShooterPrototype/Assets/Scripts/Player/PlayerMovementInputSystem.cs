using UnityEngine;
using UnityEngine.InputSystem;

public class PlayerMovementInputSystem : MonoBehaviour
{
    public float moveSpeed = 5f;
    public Rigidbody2D rb;
    public SimpleJoystick joystick; // Reference to your virtual joystick
    SimulateMobile simulateMobile; // Enable this in Inspector to test mobile input in Editor

    Vector2 movementInput;
    PlayerControls controls;

    void Awake()
    {
        controls = new PlayerControls();

        // Subscribe to keyboard movement input
        controls.Player.Move.performed += ctx => movementInput = ctx.ReadValue<Vector2>();
        controls.Player.Move.canceled += ctx => movementInput = Vector2.zero;
        simulateMobile = GetComponent<SimulateMobile>();
    }

    void OnEnable()
    {
        controls.Enable();
    }

    void OnDisable()
    {
        controls.Disable();
    }

    void Start()
    {
        if (rb == null)
            rb = GetComponent<Rigidbody2D>();
    }

    void Update()
    {
        // If running on mobile or simulating mobile input
        if (simulateMobile.simulateMobile || Application.isMobilePlatform)
        {
            if (joystick != null)
            {
                Vector2 joyInput = new Vector2(joystick.Horizontal(), joystick.Vertical());
                if (joyInput.magnitude > joystick.drift) // Apply deadzone to avoid drift
                {
                    movementInput = joyInput;
                }
                else
                {
                    movementInput = Vector2.zero;
                }
            }
        }
        // Else (PC) input is handled by Input System events set up in Awake()
    }

    void FixedUpdate()
    {
        // Move the player using physics
        Vector2 move = movementInput.normalized * moveSpeed * Time.fixedDeltaTime;
        rb.MovePosition(rb.position + move);
    }
}
