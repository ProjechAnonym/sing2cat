from config import GlobalVars
from merge import mergePart
import json,argparse,os,sys
def main():
    GlobalVars.initGlobalVars()
    base_dir = os.path.dirname(sys.argv[0])
    parser = argparse.ArgumentParser()
    parser.add_argument('--path',type=str,default=os.path.join(base_dir,'config.json'))
    args = parser.parse_args()
    config = json.dumps(mergePart.generateConfig(),ensure_ascii=False)
    with open(args.path,'w',encoding='utf-8') as f:
        f.write(config)

    
if __name__ == "__main__":
    main()