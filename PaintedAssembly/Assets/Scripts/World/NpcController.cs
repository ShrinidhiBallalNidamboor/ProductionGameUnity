using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Random = UnityEngine.Random;

[RequireComponent(typeof(Character))]
public class NpcController : MonoBehaviour, Interactable
{
    private Character _character;
    private NpcState _state;
    private void Awake() {
        _character = GetComponent<Character>();
    }

    private void Update() {
        _character.HandleUpdate();
    }

    private void Idle()
    {
        _state = NpcState.Idle;
    }

    public void Interact(Vector3 source, string name)
    {
        if (_state != NpcState.Idle)
        {
            return;
        }

        _state = NpcState.Interacting;

        _character.LookTowards(source);

        if (name == "Reception")
        {
            DialogManager.SharedInstance.ShowMenu(2, () => Idle());
        }
        else if (name == "Computer")
        {
            DialogManager.SharedInstance.ShowMenu(6, () => Idle());
        }
        else
        {
            DialogManager.SharedInstance.StartDialog(() => Idle());
        }
    }
}

public enum NpcState
{
    Idle,
    Interacting,
    Moving,
}
