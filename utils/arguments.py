import argparse

PARSER = argparse.ArgumentParser(description='entity linker')
PARSER.add_argument('--iters', type=int, default=5, help='# train iters (default: 5)')
PARSER.add_argument('--maxsteps', type=int, default=500000, help='# train iters (default: 5)')
PARSER.add_argument('--batch_size', type=int, default=1024, help='batch size (default: 1024)')
PARSER.add_argument('--seed', type=int, default=42, metavar='N', help='random seed (default: 42)')
PARSER.add_argument('--no-wvec', dest='wvec', action='store_false', help='use word vector')
PARSER.set_defaults(wvec=True)
PARSER.add_argument('--type_vocab', type=str, default="data/enwiki/fbtypelabels.vocab", help='type vocab')
PARSER.add_argument('--kb_file', type=str, required=True, help='kbfile')
PARSER.add_argument('--cold_kb_file', type=str, default=None, help='kbfile')
PARSER.add_argument('--restore', type=str, default=None, help='path restore model')
PARSER.add_argument('--restore_and_train', type=str, default=None, help='path restore model')
PARSER.add_argument('--cold_start', type=str, default=None, help='path restore model')
PARSER.add_argument('--profile', action='store_true', help='restore model')
PARSER.add_argument('--usetype', action='store_true', help='use type in model')
PARSER.add_argument('--usedesc', action='store_true', help='use desc in model')
PARSER.add_argument('--usedocbow', action='store_true', help='use doc_bow in model')
PARSER.add_argument('--usecoh', action='store_true', help='use coherence in model')
PARSER.add_argument('--uselstm', action='store_true', help='use lstm encoder')
PARSER.add_argument('--save', type=str, default=None, help='save model')
PARSER.add_argument('--ranking_loss', action='store_true', help='use desc in model')
PARSER.add_argument('--wdim', type=int, default=300, help='word vec size')
PARSER.add_argument('--hdim', type=int, default=100, help='rnn vec size')
PARSER.add_argument('--filter_num', type=int, default=100, help='conv vec size')
PARSER.add_argument('--filter_sizes', type=str, default='5', help='comma-separated conv filter sizes')
PARSER.add_argument('--cell', type=str, default="gru", help='rnn type')
PARSER.add_argument('--similarity', type=str, default="cosine", help='cosine or dot')
PARSER.add_argument('--wdrop', type=float, default=0.5, help='word dropout')
PARSER.add_argument('--cdrop', type=float, default=0.5, help='coh dropout')
PARSER.add_argument('--logsigsq', type=float, default=1.0, help='coh dropout')
PARSER.add_argument('--lr', type=float, default=0.001, help='learning rate')
PARSER.add_argument('--optimizer', type=str, default="adam", help='optimizer')
PARSER.add_argument('--pool', type=str, default="avg", help='avg or max')
PARSER.add_argument('--evalfreq', type=int, default=500, help='(default: 500)')
PARSER.add_argument('--logfreq', type=int, default=100, help='(default: 100)')
PARSER.add_argument('--cuda', dest='cuda', action='store_true', help='use cuda')
PARSER.add_argument('--cohstr', type=str, help='coh str file')
PARSER.add_argument('--ftrain', type=str, help='train file')
PARSER.add_argument('--fmix1', type=str, help='mix file')
PARSER.add_argument('--mixcands1', type=str, help='mix file')
PARSER.add_argument('--fmix2', type=str, help='mix file')
PARSER.add_argument('--mixcands2', type=str, help='mix file')
PARSER.add_argument('--fmix3', type=str, help='mix file')
PARSER.add_argument('--mixcands3', type=str, help='mix file')
# PARSER.add_argument('--mixfreq', type=int, help='mix file')
PARSER.add_argument('--mixdist', type=str, help='mix file')
PARSER.add_argument('--ftest', type=str, help='test file')
PARSER.add_argument('--fdev', type=str, help='val file')
PARSER.add_argument('--fdev2', type=str, help='val file')
PARSER.add_argument('--fdev3', type=str, help='val file')
PARSER.add_argument('--langs', type=str, default="en", help='comma sep')
PARSER.add_argument('--vocabpkl', type=str, required=True, help='eng vocab file')
PARSER.add_argument('--vecpkl', type=str, required=True, help='use word vector')
PARSER.add_argument('--trcands', type=str, required=True, help='tr surface --> cand list')
PARSER.add_argument('--ttcands', type=str, required=True, help='tt surface --> cand list')
PARSER.add_argument('--vacands', type=str, default=None, help='tt surface --> cand list')
PARSER.add_argument('--vacands2', type=str, default=None, help='tt surface --> cand list')
PARSER.add_argument('--vacands3', type=str, default=None, help='tt surface --> cand list')
PARSER.add_argument('--dump', type=str, default="", help='to dump test predictions')
PARSER.add_argument('--ncands', type=int, required=True, help='num of candidates')
PARSER.add_argument('--device_id', type=int, default=None, help='gpu device')
# "enwiki/debug_AA_mentions_full_vocab_6_wiki_00.candlist"
