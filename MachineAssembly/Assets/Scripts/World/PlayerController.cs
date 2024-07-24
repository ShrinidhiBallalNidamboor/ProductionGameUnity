using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Random = UnityEngine.Random;

[RequireComponent(typeof(Character))]
public class PlayerController : MonoBehaviour
{
    [SerializeField] private AudioClip _stepsSFX;

    [SerializeField] private Sprite _avatar;
    public Sprite Avatar => _avatar;

    [SerializeField] private string _name;
    public string Name => _name;

    private Character _character;
    private Vector2 _input;

    private void Awake() {
        _character = GetComponent<Character>();
    }

    public void HandleUpdate() {
        if (!_character.IsMoving)
        {
            _input.x = Mathf.RoundToInt(Input.GetAxisRaw("Horizontal"));
            _input.y = Mathf.RoundToInt(Input.GetAxisRaw("Vertical"));

            if (_input != Vector2.zero)
            {
                StartCoroutine(_character.MoveTowards(_input,
                    () => AudioManager.SharedInstance.PlaySFX(_stepsSFX)
                ));
            }

            if (Input.GetButtonDown("Submit"))
            {
                Interact();
            }
        }

        _character.HandleUpdate();
    }

    private void Interact()
    {
        var facingDirection = new Vector3(_character.Animator.MoveX, _character.Animator.MoveY);
        var interactPosition = transform.position + facingDirection;

        Debug.DrawLine(transform.position, interactPosition, Color.magenta, 1.0f);

        var collider = Physics2D.OverlapCircle(interactPosition, 0.25f, LayerManager.SharedInstance.InteractableLayers);

        if (collider != null)
        {
            collider.GetComponent<Interactable>()?.Interact(transform.position, collider.gameObject.name);
        }
    }
}
