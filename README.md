# py-github-actions-starter

Github Actions Docker/Python Template

This action waits for the specified time and prints out the time when run
was finished.

## Inputs

### `seconds`

**Required** The time that action should wait.

## Outputs

### `time`

The time when run was finished.

## Example usage

```yaml
uses: lsetiawan/py-github-actions-starter@v1
with:
  time: '5'
```
