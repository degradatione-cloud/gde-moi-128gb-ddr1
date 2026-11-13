from pathlib import Path

LINE = 'Где мои 128 гб ддр1\n'.encode('utf-8')
COUNT = 1_000_000
CHUNK_LINES = 4096
path = Path(__file__).with_name('ddr1.txt')
with path.open('wb') as f:
    chunk = LINE * CHUNK_LINES
    full, tail = divmod(COUNT, CHUNK_LINES)
    for _ in range(full):
        f.write(chunk)
    f.write(LINE * tail)

count = 0
with path.open('rb') as f:
    for count, line in enumerate(f, 1):
        if line != LINE:
            raise RuntimeError(f'Unexpected content at line {count}')
assert count == COUNT, count
assert path.stat().st_size == len(LINE) * COUNT
print(f'Verified: {count:,} identical lines; {path.stat().st_size:,} bytes')
