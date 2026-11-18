# Build into build/, mirroring the source folders (needed for \include).
$pdf_mode = 1;
$out_dir = 'build';
use File::Find; use File::Path qw(make_path);
find({ no_chdir => 1, wanted => sub {
  return unless -d $_;
  if (m{^\./(build|\.git)}) { $File::Find::prune = 1; return; }
  make_path("build/$_");
}}, '.');
